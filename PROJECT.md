# RXD Cloud Consulting website — plan, progress and roadmap

Living document. `README.md` covers *how to run and deploy*; this covers *why the site is
built this way, what state it's in, and what comes next*.

**Last updated:** 2026-07-31
**Status:** Built, not yet deployed — blocked on the account setup in [§3](#3-blocked-on-your-input).

---

## 1. Context and goal

The site exists to turn a LinkedIn visitor into a conversation about a Workday engagement.
That is its only job. Every decision below is measured against it.

The starting point was a well-written single-page CV: services, three result figures, an
about block, and a `mailto:` link. It described the practice accurately but did nothing to
convert. The specific failures:

| Problem | Consequence |
| --- | --- |
| `mailto:` was the only contact route | Silently fails for mobile and webmail users — most of the LinkedIn audience |
| Mobile nav hid every link except the CTA | Navigation simply did not exist below 640px |
| Result figures had no story behind them | "~700 hires/year" is impressive but unverifiable and unmemorable |
| No testimonials, no photo | Nothing but self-assertion to trust |
| Rates, contract vehicle, DBA status unanswered | Cautious buyers bounce rather than ask |
| No `og:image`, no structured data | A link posted to LinkedIn rendered as a bare grey box |
| No analytics | No way to learn what works |

---

## 2. Progress

### Shipped

**Conversion**
- Web3Forms contact form — AJAX submit with inline success/error, honeypot field, native
  HTML5 validation. Degrades to a plain form POST with JavaScript disabled.
- Cal.com "book a 20-min intro call" button, in the hero, the contact block and the mobile bar.
- Sticky mobile CTA bar below 640px.
- Email address kept visible with a copy-to-clipboard button.
- Availability badge in the hero.

**Proof**
- Three case studies in Situation / Action / Result form (Picnic, Munters, Barings), each
  led by its headline figure so the number and the story reinforce each other.
- Testimonial block — **placeholder text, see §3**.
- Photo slot in About — **commented out until a file exists, see §3**.

**Objection handling**
- Six-question FAQ as a no-JS `<details>` accordion: pricing, agencies and intermediaries,
  Dutch DBA rules, lead time and minimum engagement, time zones, what's needed to start.

**Discovery and sharing**
- JSON-LD: `ProfessionalService` + `Person` + `FAQPage`, cross-linked by `@id`.
- Canonical URL, full Open Graph and Twitter card meta, `robots.txt`, `sitemap.xml`.
- `og-image.png` (1200×627) generated from HTML so it stays in the site's visual style.

**Accessibility and mobile**
- Mobile nav rebuilt as a `<details>` disclosure — the regression fix.
- Skip link, visible `:focus-visible` rings, semantic landmarks, `prefers-reduced-motion`
  guards on scroll behaviour and transitions.
- Colour contrast checked against WCAG AA in both themes.

**LinkedIn**
- `LINKEDIN.md` — page identity fields, tagline, ~1,930-character About section, 20
  Specialties tags, UTM'd button config, first-five-posts plan, profile linking checklist.
- `linkedin-logo.png` (300×300) and `linkedin-banner.png` (1128×191), generated from HTML.

**Analytics**
- Cloudflare Web Analytics beacon, plus conversion tracking on the four routes in
  (see the analytics note in `README.md` for the `/goal/*` workaround and its caveat).

### Verified

- JSON-LD parses; FAQ entries in the markup and in the structured data match (6 = 6).
- Rendered at 1440px, 1200px and 500px. Mobile menu opens and all five links are reachable.
- Share card, LinkedIn logo and banner render correctly at their target dimensions.

### Not yet verified — needs a live deploy

Structured data in Google's Rich Results Test · LinkedIn Post Inspector · a real form
submission · Lighthouse · analytics reaching the dashboard. Checklist in `README.md`.

---

## 3. Blocked on your input

| # | Needed | Where to get it |
| --- | --- | --- |
| 1 | Domain | Decide, then find-and-replace `SITE_URL` |
| 2 | Web3Forms access key | [web3forms.com](https://web3forms.com) — free, no account |
| 3 | Cal.com booking link | [cal.com](https://cal.com) — 20-min "Intro call" event type |
| 4 | Cloudflare Analytics token | Cloudflare dashboard → Web Analytics |
| 5 | Availability date | The month you're next free |
| 6 | Professional photo | Square, ≥320×320, as `rafael-sebastian.jpg` |
| 7 | 2–3 testimonials | Existing LinkedIn recommendations, quoted with permission |

**Items 6 and 7 are the weakest part of the site.** The testimonial block currently ships
with visible `TESTIMONIAL_*` placeholders — delete the block rather than deploy it as-is.
Social proof is the single highest-value addition still outstanding.

---

## 4. Roadmap

### Next — before or shortly after launch

- **Fill the placeholders and deploy.** Nothing else matters until the site is live.
- **`thanks.html`** — a real destination for the no-JS form fallback, and a clean
  conversion event to count.
- **`404.html`.**
- **Security headers** — a `_headers` file (Cloudflare Pages) or equivalent, with a CSP,
  `X-Content-Type-Options` and `Referrer-Policy`.
- **Search Console + Bing Webmaster Tools**, sitemap submitted to both.
- **Client logos** instead of the plain-text experience strip — check your contracts for
  name-use permission first; not every client allows it.

### Mid — the growth levers

- **Writing.** The highest-return addition by a distance. Long-tail search for Workday
  integration problems ("Workday Studio memory limits", "EIB vs Core Connector for X") is
  low-volume and extremely high-intent — the people searching it have the problem *now*.
  Two or three genuinely useful technical posts will outperform any amount of site polish.
  Needs a `/writing` index, per-post pages, and `Article` schema.
- **Expanded case study pages.** The cards are deliberately short. One full page per
  engagement — architecture, constraints, what you'd do differently — is what a technical
  buyer reads before deciding you're credible.
- **Productised offerings.** Fixed-scope, fixed-price packages ("Integration health check",
  "Workday release readiness review"). Far easier to say yes to than an open-ended day rate,
  and they make a good first engagement that leads to longer work.
- **Lead magnet.** A genuinely useful download — an integration pre-flight checklist, a
  release-testing template — in exchange for an email. Turns the ~97% who leave without
  contacting you into a list you can talk to later.
- **`Review` / `AggregateRating` schema** once real testimonials exist.

### Later — worth considering, not obviously worth doing

- **Dutch-language version** with `hreflang`. Deferred: you work in English worldwide, and
  it doubles maintenance. Revisit if NL agency traffic turns out to dominate.
- **Inline Cal.com embed** rather than an outbound link — fewer clicks, but a heavier page
  and a third-party script.
- **Plausible instead of Cloudflare Web Analytics** if conversion tracking becomes central;
  it has a real custom-event API and would remove the `/goal/*` workaround.
- **Automated deploy** via GitHub Actions — only worth it if the site starts changing often.
- **A build step.** Currently none, deliberately. If the writing section lands and content
  starts repeating, a small static generator (Eleventy) becomes justified. Not before.

---

## 5. Decisions and rationale

Recorded so they don't get silently re-litigated later.

| Decision | Why |
| --- | --- |
| No build step, plain HTML/CSS/JS | The site is small and changes rarely. A toolchain would add maintenance and rot between edits. Revisit only if a blog lands. |
| Web3Forms over Formspree | Free and unlimited, no dashboard account, key arrives by email. Formspree's free tier caps at 50 submissions/month. |
| Cal.com over Calendly | Open source, free tier, EU hosting available — easier to defend under GDPR to an enterprise buyer. |
| Cloudflare Web Analytics over GA4 | Cookieless, so no consent banner. GA4 would add friction on the exact page meant to convert. |
| JS as progressive enhancement only | The whole page works without `main.js`. A sales page must never be one script error away from having no contact route. |
| `<details>` for nav and FAQ | Keyboard-accessible and indexable with zero JavaScript. |
| Images generated from HTML | Share card, logo and banner stay consistent with the site and are regenerable from source rather than being opaque binaries. |
| English only | You work remotely worldwide in English; a second language doubles the maintenance surface. |
| Org and Person are separate JSON-LD entities | The company page is not the personal profile. Conflating them would be factually wrong in the structured data. |

---

## 6. File map

| File | Purpose |
| --- | --- |
| `index.html` | The entire site |
| `styles.css` | Responsive, light/dark aware |
| `main.js` | Progressive enhancement only — form, nav, copy button, tracking |
| `favicon.svg` | RX monogram |
| `og-image.html` → `.png` | Social share card, 1200×627 |
| `linkedin-banner.html` → `.png` | LinkedIn cover, 1128×191 |
| `linkedin-logo.html` → `.png` | LinkedIn logo, 300×300 |
| `robots.txt`, `sitemap.xml` | Crawler basics |
| `README.md` | Setup, placeholders, deploy, image regeneration |
| `LINKEDIN.md` | Company page copy and launch checklist |
| `PROJECT.md` | This document |
