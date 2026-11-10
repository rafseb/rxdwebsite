#!/usr/bin/env python3
"""Static checks for the RXD website. Run locally or in CI.

Exit 1 on any ERROR. WARN lines never fail the build.
Usage: python3 scripts/check_site.py [site_root]
"""
import json
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), ".."))
PAGES = ["index.html", "privacy.html"]
VOID = {"meta", "link", "img", "input", "br", "hr", "source", "area", "base", "col", "embed", "track", "wbr"}

# Must never reach the published site.
FORBIDDEN_PLACEHOLDERS = [
    "SITE_URL", "WEB3FORMS_ACCESS_KEY", "CAL_BOOKING_URL",
    "CLOUDFLARE_ANALYTICS_TOKEN", "AVAILABILITY_DATE", "TESTIMONIAL_",
]
# Owner chose to leave these until a business address exists. Warn only.
WARN_PLACEHOLDERS = [r"\bSTREET_ADDRESS\b", r"\bPOSTAL_CODE\b", r"\bCITY\b"]
# Third parties that the privacy notice says are not contacted by the site.
FORBIDDEN_HOSTS = ["fonts.googleapis.com", "fonts.gstatic.com"]

errors, warnings = [], []


def error(msg):
    errors.append(msg)
    print(f"ERROR: {msg}")


def warn(msg):
    warnings.append(msg)
    print(f"WARN:  {msg}")


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


class TagBalance(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.mismatch = [], []
        self.refs = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for key in ("href", "src"):
            if key in a and a[key]:
                self.refs.append(a[key])
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        else:
            self.mismatch.append(tag)


def local_ref_exists(ref):
    if re.match(r"^(https?:|mailto:|tel:|data:|#|//)", ref):
        return True
    path = ref.split("#")[0].split("?")[0]
    if not path:
        return True
    return os.path.exists(os.path.join(ROOT, path))


def check_html(page):
    text = read(page)
    parser = TagBalance()
    parser.feed(text)
    if parser.stack:
        error(f"{page}: unclosed tags {parser.stack}")
    if parser.mismatch:
        error(f"{page}: mismatched closing tags {parser.mismatch[:5]}")

    for ref in parser.refs:
        if not local_ref_exists(ref):
            error(f"{page}: local reference not found: {ref}")

    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
        try:
            json.loads(m.group(1))
        except json.JSONDecodeError as e:
            error(f"{page}: JSON-LD does not parse: {e}")

    if 'http-equiv="Content-Security-Policy"' not in text:
        error(f"{page}: missing Content-Security-Policy meta tag")

    for host in FORBIDDEN_HOSTS:
        if host in text:
            error(f"{page}: references {host}, self-host instead (privacy notice says no Google font requests)")


def check_css_refs():
    # url() paths resolve relative to the stylesheet's own folder.
    for sheet in ["styles.css", "fonts/space-grotesk.css"]:
        css = read(sheet)
        base = os.path.dirname(sheet)
        for host in FORBIDDEN_HOSTS:
            if host in css:
                error(f"{sheet}: references {host}")
        for m in re.finditer(r"url\(([^)]+)\)", css):
            ref = m.group(1).strip("'\"")
            if re.match(r"^(https?:|data:)", ref):
                continue
            if not os.path.exists(os.path.join(ROOT, base, ref)):
                error(f"{sheet}: url not found: {ref}")


def check_placeholders():
    for page in PAGES + ["sitemap.xml", "robots.txt"]:
        text = read(page)
        for token in FORBIDDEN_PLACEHOLDERS:
            if token in text:
                error(f"{page}: placeholder {token} still present")
        for pattern in WARN_PLACEHOLDERS:
            token = pattern.replace(r"\b", "")
            if re.search(pattern, text):
                warn(f"{page}: address placeholder {token} still present (owner decision, not deploy-blocking)")


def main():
    for page in PAGES:
        check_html(page)
    check_css_refs()
    check_placeholders()
    if errors:
        print(f"\n{len(errors)} error(s), {len(warnings)} warning(s). FAIL.")
        sys.exit(1)
    print(f"\nOK. {len(warnings)} warning(s).")


if __name__ == "__main__":
    main()
