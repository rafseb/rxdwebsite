# RXD Cloud Consulting — website

Single-page static site for RXD Cloud Consulting (Workday integration consulting).
No build step — plain HTML/CSS/JS.

## Before going live

The site contains placeholder tokens that must be replaced. Check none survive:

```sh
grep -rn "SITE_URL\|WEB3FORMS_ACCESS_KEY\|CAL_BOOKING_URL\|CLOUDFLARE_ANALYTICS_TOKEN\|AVAILABILITY_DATE\|TESTIMONIAL_" \
  --include="*.html" --include="*.js" --include="*.txt" --include="*.xml" --include="*.md" .
```

| Token | Where to get it | Files |
| --- | --- | --- |
| `SITE_URL` | Your domain, no trailing slash (e.g. `https://rxdconsulting.nl`) | `index.html`, `robots.txt`, `sitemap.xml`, `LINKEDIN.md` |
| `WEB3FORMS_ACCESS_KEY` | Free at [web3forms.com](https://web3forms.com) — no account, the key is emailed to you | `index.html` |
| `CAL_BOOKING_URL` | [cal.com](https://cal.com) — create a 20-minute "Intro call" event type | `index.html` (3 places) |
| `CLOUDFLARE_ANALYTICS_TOKEN` | Cloudflare dashboard → Web Analytics → add site | `index.html` |
| `AVAILABILITY_DATE` | The month you're next free, e.g. `September 2026` | `index.html` |
| `TESTIMONIAL_*` | Real quotes + permission. Delete the `.testimonials` block rather than shipping placeholders | `index.html` |

Photo: add `rafael-sebastian.jpg` (square, ≥320×320) and optionally a `.webp` version, then
uncomment the `<picture>` block in the About section of `index.html`. It ships commented out so
a deploy without the file can't show a broken image.

## Preview locally

```sh
python3 -m http.server 8080
# then open http://localhost:8080
```

The contact form and analytics won't work over `file://` — use the server.

## Regenerating images

All three share images are generated from HTML so they stay in the site's visual style.

```sh
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Social share card (LinkedIn, Slack, WhatsApp link previews)
"$CHROME" --headless --disable-gpu --hide-scrollbars \
  --screenshot=og-image.png --window-size=1200,627 og-image.html

# LinkedIn company page cover
"$CHROME" --headless --disable-gpu --hide-scrollbars \
  --screenshot=linkedin-banner.png --window-size=1128,191 linkedin-banner.html

# LinkedIn company page logo
"$CHROME" --headless --disable-gpu --hide-scrollbars \
  --screenshot=linkedin-logo.png --window-size=300,300 linkedin-logo.html
```

## Deploy (free options)

**GitHub Pages**

```sh
gh repo create rxdwebsite --public --source . --push
# then enable Pages in repo Settings → Pages → branch: main
```

**Cloudflare Pages** — create a project at dash.cloudflare.com → Pages, connect the repo,
no build command, output directory `/`. Recommended if you're using Cloudflare Web Analytics,
since the beacon is then injected and configured for you.

Afterwards, point a custom domain at the host via DNS.

### After the first deploy

1. Run the live URL through [LinkedIn Post Inspector](https://www.linkedin.com/post-inspector/)
   — it verifies the share card renders *and* busts LinkedIn's aggressive Open Graph cache.
   Re-run it after any change to the `og:` meta tags.
2. Validate the structured data at [validator.schema.org](https://validator.schema.org/)
   and Google's Rich Results Test.
3. Submit `sitemap.xml` in Google Search Console.

## Analytics note

Cloudflare Web Analytics has no custom-event API. `main.js` records conversions as virtual
pageviews under `/goal/*` (using `history.pushState`, which the beacon tracks when
`"spa": true`), then restores the real URL immediately. In the dashboard, read pageviews on:

- `/goal/book-call` — clicked through to the booking page
- `/goal/contact-form` — submitted the contact form successfully
- `/goal/email` — clicked the email address
- `/goal/linkedin` — clicked through to LinkedIn

## Files

- `index.html` — all content (hero, services, case studies, testimonials, about, FAQ, contact, legal footer)
- `styles.css` — responsive, light/dark aware styling
- `main.js` — progressive enhancement only: AJAX form submit, mobile nav, copy-to-clipboard, conversion tracking. The site works without it.
- `favicon.svg` — RX monogram
- `og-image.html` / `og-image.png` — social share card (1200×627)
- `linkedin-banner.html` / `linkedin-banner.png` — LinkedIn cover (1128×191)
- `linkedin-logo.html` / `linkedin-logo.png` — LinkedIn logo (300×300)
- `robots.txt`, `sitemap.xml` — crawler basics
- `LINKEDIN.md` — paste-ready copy and setup checklist for the LinkedIn company page
- `PROJECT.md` — plan, progress, roadmap and the rationale behind the build decisions
