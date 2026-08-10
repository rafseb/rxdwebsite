# Deployment Checklist

Site is ready to push and enable on GitHub Pages, with 2 signup-required placeholders remaining.

## ✅ Completed

- [x] Site URL → `https://rafseb.github.io/rxdwebsite` (14 locations)
- [x] Booking links → Calendly `https://calendly.com/raf-sebastian/30min` (3 buttons)
- [x] Button text → Changed from "20-min" to "30-min intro call"
- [x] Availability → "Available now · Remote worldwide"
- [x] LinkedIn URL → Updated to full profile URL
- [x] Testimonials → Removed (add back when you have real quotes with permission)
- [x] KvK & BTW → Already present (KVK 99369494, BTW NL005382072B24)

## ⏳ Remaining (2 external signups)

### 1. Contact form — Web3Forms access key

**Where:** Line 393 of `index.html`

```html
<input type="hidden" name="access_key" value="WEB3FORMS_ACCESS_KEY">
```

**Get it:**
1. Go to [web3forms.com](https://web3forms.com)
2. Enter `rscloudsolutions@gmail.com` (the email already wired in the form)
3. Access key arrives instantly at that email
4. Replace `WEB3FORMS_ACCESS_KEY` in line 393 with the key

**Without this:** The contact form shows but submissions fail silently.

---

### 2. Cloudflare Web Analytics token

**Where:** Line 464 of `index.html`

```html
<script defer src='https://static.cloudflareinsights.com/beacon.min.js'
        data-cf-beacon='{"token": "CLOUDFLARE_ANALYTICS_TOKEN", "spa": true}'></script>
```

**Get it:**
1. Log in to Cloudflare dashboard
2. Analytics → Web Analytics → "Add a site"
3. Enter site name (e.g. "RXD Cloud Consulting")
4. Copy the token from the JS snippet they show
5. Replace `CLOUDFLARE_ANALYTICS_TOKEN` in line 464

**Without this:** The analytics script loads but doesn't send data. The site works fine; you just have no visit stats.

---

## 🚀 Deploy to GitHub Pages

The repo is already on GitHub at `rafseb/rxdwebsite` (private). To go live:

1. **Commit and push** (commands below)
2. **Enable GitHub Pages:**
   - Go to repo Settings → Pages
   - Source: **Deploy from branch**
   - Branch: **main**, folder: **/ (root)**
   - Save
3. **Wait 2-3 minutes** for the first deploy
4. Site lives at `https://rafseb.github.io/rxdwebsite`

```bash
cd "/Users/raf/rxdwebsite"

git add -A
git commit -m "Ready for launch: site URL, Calendly booking, availability, LinkedIn URL

- Set site URL to GitHub Pages (https://rafseb.github.io/rxdwebsite)
- Updated booking links to Calendly 30-min intro call (3 locations)
- Changed availability from placeholder to 'Available now'
- Updated LinkedIn URL to full profile
- Removed testimonials block (placeholder quotes)
- KvK 99369494 and BTW already present in footer

Remaining: Web3Forms and Cloudflare tokens (documented in DEPLOY-CHECKLIST.md)"

git push origin main
```

---

## 📋 After first deploy (do once)

1. **Test the contact form** after adding the Web3Forms key — submit a test inquiry
2. **LinkedIn Post Inspector:** Run `https://rafseb.github.io/rxdwebsite` through [linkedin.com/post-inspector](https://www.linkedin.com/post-inspector/) to bust the OG cache and verify the share card renders
3. **Schema validation:** [validator.schema.org](https://validator.schema.org/) + [Google Rich Results Test](https://search.google.com/test/rich-results)
4. **Google Search Console:** Submit `sitemap.xml` once the domain is indexed

---

## 🌐 Custom domain (optional, later)

When you buy a domain (e.g. `rxdconsulting.nl`):

1. Add a `CNAME` file to the repo containing your domain:
   ```bash
   echo "rxdconsulting.nl" > CNAME
   git add CNAME && git commit -m "Add custom domain" && git push
   ```
2. In your DNS provider, add a `CNAME` record:
   - Name: `@` (or `www`)
   - Target: `rafseb.github.io`
3. GitHub Settings → Pages → Custom domain → enter your domain → Save
4. Enable "Enforce HTTPS" once DNS propagates (takes ~1 hour)
5. **Then** replace all `https://rafseb.github.io/rxdwebsite` URLs with your domain in:
   - `index.html` (14 locations)
   - `robots.txt`
   - `sitemap.xml`

---

## 🔍 Quick verification

Before pushing, confirm no critical placeholders remain:

```bash
grep -rn "SITE_URL\|WEB3FORMS_ACCESS_KEY\|CAL_BOOKING_URL\|CLOUDFLARE_ANALYTICS_TOKEN\|AVAILABILITY_DATE\|TESTIMONIAL_" \
  --include="*.html" --include="*.js" --include="*.txt" --include="*.xml" .
```

Expected output: only `WEB3FORMS_ACCESS_KEY` (line 393) and `CLOUDFLARE_ANALYTICS_TOKEN` (line 464).
