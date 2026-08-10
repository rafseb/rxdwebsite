# LinkedIn company page kit — RXD Cloud Consulting

Paste-ready copy and assets for setting up the LinkedIn company page.
Create it at **linkedin.com/company/setup/new** → *Company*.

Replace `SITE_URL` throughout with the live domain once it's chosen.

---

## 1. Page identity

| Field | Value |
| --- | --- |
| **Name** | `RXD Cloud Consulting` |
| **LinkedIn public URL** | `linkedin.com/company/rxd-cloud-consulting` |
| **Website** | `SITE_URL/?utm_source=linkedin&utm_medium=social&utm_campaign=company-page` |
| **Industry** | IT Services and IT Consulting |
| **Company size** | 1 employee |
| **Company type** | Self-employed |
| **Headquarters** | The Netherlands (remote-first) |
| **Founded** | *(year of KVK registration — check your KVK extract)* |
| **Phone** | *(optional — leave blank if you'd rather route everything through email)* |

### Tagline (max 120 characters)

```
Freelance Workday integration consulting — Studio, EIB, Core Connectors. Workday Pro Certified, 15+ years.
```

*(105 characters.)*

---

## 2. About section (max 2,000 characters)

```
RXD Cloud Consulting is the practice of Rafael Sebastian, a Workday Pro Certified integration consultant with 15+ years in HR technology.

We help People Systems, HR, Payroll and Finance teams make Workday work with everything around it — from integration architecture through to zero-touch automation that runs without anyone watching it.

WHAT WE DO

• Workday Integration Development — end-to-end builds with Workday Studio, EIB, Core Connectors, XSLT and Document Transform, from specification to production support.

• Integration Architecture — design of multi-system HR landscapes connecting Workday to ServiceNow, Salesforce, ADP, CloudPay, Greenhouse, Active Directory and more.

• Workday Application Management — SME ownership of your tenant: security, business processes, release management, and enabling your internal team.

• HR Process Automation & Reporting — turning manual HR and Finance processes into zero-touch automation, plus workforce reporting including CSRD data extraction.

RESULTS THAT SHIPPED

• ~700 new hires per year with day-1 system access at Picnic, with onboarding login failures eliminated.
• CSRD workforce data tooling at Munters, published in the Munters Annual & Sustainability Report 2025.
• 5–15 hours of manual HR and Finance processing saved every week at Barings.

BACKGROUND

Since 2009, across the full HR technology stack — starting in PeopleSoft and Oracle at Accenture, and specialising in Workday integrations for the past decade at Agoda, Barings, Picnic and Munters.

Certifications: Workday Pro (HCM Core & Integration), Workday Financial Fundamentals.

HOW WE WORK

Freelance and interim assignments, remote worldwide, in English. Based in the Netherlands (CET/CEST). We contract directly with end clients as well as through agencies and payroll intermediaries.

Registered in the Netherlands — KVK 99369494 · BTW NL005382072B24.

Let's talk about your project: SITE_URL
```

*(~1,930 characters — check the counter after any edit.)*

---

## 3. Specialties (up to 20)

These feed LinkedIn's internal search and are the most under-used field on the whole page. Add every one:

```
Workday
Workday Integrations
Workday Studio
Workday EIB
Workday Core Connector
Workday Report Writer
Workday Orchestrate
HCM Integration
Integration Architecture
HR Technology
HRIS Consulting
Payroll Integration
XSLT
Document Transform
HR Process Automation
Workday Security
Workday Business Process
CSRD Reporting
Workforce Reporting
Freelance Workday Consultant
```

---

## 4. Visual assets

Both are already generated in this repo, in the same style as the website:

| Asset | File | Size | Notes |
| --- | --- | --- | --- |
| Logo | `linkedin-logo.png` | 300×300 | Regenerate: see the comment in `linkedin-logo.html` |
| Cover / banner | `linkedin-banner.png` | 1128×191 | Regenerate: see the comment in `linkedin-banner.html` |

The banner deliberately keeps its left ~250px free of text, because LinkedIn overlays the page logo there and crops the image differently on mobile.

---

## 5. Custom button

Page admin view → **Edit page** → *Buttons*:

- **Button:** `Visit website`
- **URL:** `SITE_URL/?utm_source=linkedin&utm_medium=social&utm_campaign=page-button`

Using a distinct `utm_campaign` per placement is what lets you tell, in Cloudflare Web Analytics, whether the button or the About-section link is doing the work.

---

## 6. First five posts

Post these over the first two to three weeks — a page with no posts reads as abandoned, and LinkedIn suppresses reach for pages with no activity.

**Post 1 — Launch.** What RXD Cloud Consulting is, who it's for, and that you're available. End with the site link. Post this from the company page, then reshare from your personal profile with a short personal note — your personal network is where the initial reach comes from.

**Post 2 — Picnic case study.** The day-1 access problem. Open with the specific pain (a new starter who can't log in on their first morning), then the fix, then the number. Roughly 150–200 words.

**Post 3 — Munters case study.** CSRD workforce reporting. This one has the widest audience right now — every HR team in the EU is working out how to produce these numbers. Lead with the reporting problem, not the Workday feature.

**Post 4 — Barings case study.** The 5–15 hours a week. Frame it as "here's what manual processing actually costs you", and invite people to name the process they're still doing by hand.

**Post 5 — Availability.** What you're available for, from when, and the kinds of engagement that fit (integration build, architecture review, interim application management). Link to the booking page.

**After that:** roughly one post a week. The highest-value content for this audience is specific and technical — a Workday Studio gotcha, an EIB limit and the way around it, what changes in a Workday release. Being useful in public is what makes the case-study posts land when they come.

---

## 7. Connect it to your personal profile

The company page on its own gets very little traffic. The personal profile is the funnel.

- [ ] **Experience entry** — add "Owner / Workday Integration Consultant" at RXD Cloud Consulting and select the new company page, so its logo appears on your profile and the page gains a linked employee.
- [ ] **Headline** — make sure it says what you sell and that you're available, e.g. `Freelance Workday Integration Consultant | Workday Pro Certified | Studio, EIB, Core Connectors | Available for projects`.
- [ ] **Featured section** — pin the website link and the launch post.
- [ ] **Profile CTA** — turn on the "Open to work" → *contract/freelance* setting if you want recruiter traffic, or set the profile button to your website if you'd rather they come to you.
- [ ] **About section** — reuse the opening two paragraphs of §2 above so the story matches wherever someone lands.
- [ ] **Recommendations** — ask two or three former colleagues from Munters, Picnic or Barings. These double as the website testimonials (see the `TESTIMONIAL_*` placeholders in `index.html`).
- [ ] **Invite connections to follow the page** — page admin view → *Invite connections*. You get a monthly credit allowance; spend it on people in HRIS/People Systems roles.
