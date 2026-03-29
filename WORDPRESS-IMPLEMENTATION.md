# Key's Touch — WordPress Implementation Guide

## Overview
This guide walks you through implementing the redesigned keystouch.com on WordPress. Every HTML file in this directory is a content/design reference — you'll recreate these pages using WordPress + a page builder.

---

## Step 1: Theme Setup

### Recommended Theme: **Kadence Pro** (or Astra Pro)
- Lightweight (< 50KB CSS)
- Full header/footer builder
- Global color/typography controls
- WooCommerce compatible if needed later

**Install:**
1. WordPress Admin > Appearance > Themes > Add New
2. Search "Kadence" > Install & Activate
3. Install "Kadence Pro" addon for header builder + advanced features

### Global Settings (Appearance > Customize)
```
Colors:
  - Background: #0A0A0A
  - Surface: #111113
  - Text Primary: #FFFFFF
  - Text Secondary: #B0B0C0
  - Accent 1 (Cyan): #00B4D8
  - Accent 2 (Purple): #7C3AED

Typography:
  - Headings: Space Grotesk (600/700 weight)
  - Body: Inter (400/500 weight)
  - Base size: 16px
```

---

## Step 2: Page Builder

### Recommended: **Elementor Pro** ($59/year)
Best balance of power and ease-of-use for this design.

**Alternative:** Bricks Builder ($99 one-time) — faster performance, steeper learning curve.

**Install:**
1. Plugins > Add New > Search "Elementor"
2. Install free version, then upload Pro license

### Elementor Global Settings
- Default Colors: Match the color scheme above
- Default Fonts: Space Grotesk + Inter
- Container Layout: Boxed, 1200px max-width
- Default padding: 120px top/bottom for sections

---

## Step 3: Required Plugins

| Plugin | Purpose | Cost |
|--------|---------|------|
| Kadence Pro | Theme framework | $79/year |
| Elementor Pro | Page builder | $59/year |
| RankMath Pro | SEO (sitemaps, schema, redirects) | $59/year |
| WP Rocket | Caching & speed optimization | $59/year |
| WPForms Pro | Contact forms | $49/year |
| Calendly (embed) | Booking integration | Free tier works |
| GA4 + Site Kit | Analytics | Free |
| Microsoft Clarity | Heatmaps & session recording | Free |
| Cloudflare | CDN & security | Free tier |
| UpdraftPlus | Backups | Free |
| Redirection | 301 redirects from old URLs | Free |
| ShortPixel | Image compression | Free tier |

---

## Step 4: Page Build Order

### 1. Homepage (index.html)
This is the reference. Build each section as an Elementor section:
- **Nav:** Use Kadence Header Builder (sticky, transparent on hero)
- **Hero:** Full-height section with gradient orbs (use CSS in custom code widget)
- **Trust Bar:** Logo carousel or simple text row
- **Problem/Solution:** 3-column card grid
- **Services:** 2x3 card grid with hover effects
- **Results:** 3-column metric cards
- **Testimonials:** 3-column testimonial cards
- **Process:** 4-step horizontal layout
- **CTA:** Full-width section with radial gradient background
- **Footer:** Use Kadence Footer Builder

### 2. Service Pages (services/*.html)
Create as Elementor templates — build one, duplicate for others:
- Service Hero (shorter, 70vh)
- Use Cases / Features grid
- Process steps
- Tech stack section
- Bottom CTA

### 3. About Page (about.html)
- Hero with mission statement
- 2-column mission + stats layout
- 6-card values grid
- Founder section
- CTA

### 4. Contact Page (contact.html)
- Hero
- 2-column layout: Calendly embed + contact form on left, info cards on right
- WPForms for the contact form (or Fluent Forms)
- Calendly inline embed widget

### 5. Case Studies (case-studies.html)
- Hero
- Alternating left/right case study cards
- Replace placeholder images with real screenshots as you complete projects
- CTA

---

## Step 5: SEO Setup (RankMath)

1. **Install RankMath Pro** > Run setup wizard
2. **Set Homepage SEO:**
   - Title: `Key's Touch | AI Automation & Software Consulting`
   - Description: `We engineer AI-powered systems that eliminate manual work and scale revenue. Custom AI agents, automation workflows, and software solutions.`
3. **Enable Schema Markup:**
   - Organization schema on homepage
   - LocalBusiness schema
   - Service schema on service pages
   - FAQ schema on contact page
4. **Create XML Sitemap** (RankMath > Sitemap Settings)
5. **Submit to Google Search Console**

---

## Step 6: Speed Optimization

### WP Rocket Settings:
- Enable page caching
- Enable browser caching
- Minify CSS & JS
- Defer JavaScript loading
- Lazy load images
- Enable CDN (Cloudflare)

### Image Optimization:
- Use WebP format (ShortPixel converts automatically)
- Max width: 1200px for full-width images
- Compress to < 100KB per image
- Use lazy loading for below-fold images

### Target Performance:
- Google PageSpeed: 90+ (mobile & desktop)
- Largest Contentful Paint: < 2.5s
- Cumulative Layout Shift: < 0.1

---

## Step 7: Analytics & Tracking

### Google Analytics 4:
1. Create GA4 property
2. Install via Google Site Kit plugin
3. Set up conversion events:
   - `form_submit` (contact form)
   - `calendly_booking` (Calendly event)
   - `cta_click` (track all CTA button clicks)

### Microsoft Clarity:
1. Create Clarity project
2. Add tracking code via header injection (Kadence > Custom Scripts)
3. Monitor heatmaps and session recordings weekly

### Conversion Tracking Checklist:
- [ ] Contact form submissions tracked
- [ ] Calendly bookings tracked
- [ ] CTA button clicks tracked
- [ ] Page scroll depth tracked
- [ ] Service page visits tracked

---

## Step 8: Redirects (Critical)

Set up 301 redirects from all old URLs to new ones:

```
/product     → /case-studies
/contact     → /contact (same)
/about-us    → /about
```

Use the Redirection plugin to manage these.

---

## Step 9: Pre-Launch Checklist

- [ ] All pages built and reviewed on mobile
- [ ] Contact form tested (submissions received)
- [ ] Calendly embed working
- [ ] SEO titles & descriptions set for all pages
- [ ] Schema markup validated (Google Rich Results Test)
- [ ] Page speed 90+ on mobile
- [ ] Analytics tracking confirmed
- [ ] 301 redirects in place
- [ ] Favicon & social sharing images uploaded
- [ ] Open Graph tags set for social sharing
- [ ] SSL certificate active (HTTPS)
- [ ] XML sitemap submitted to Google Search Console
- [ ] Backup system configured

---

## Step 10: Post-Launch (First 30 Days)

1. **Week 1:** Monitor analytics, fix any broken links, check form submissions
2. **Week 2:** Review Clarity heatmaps, optimize CTA placement based on data
3. **Week 3:** Publish first blog post / insight for SEO
4. **Week 4:** Review conversion rates, adjust copy/CTAs based on performance

---

## File Structure Reference

```
company-site/
├── SITE-STRATEGY.md          ← Positioning, architecture, design direction
├── WORDPRESS-IMPLEMENTATION.md ← This file
├── index.html                ← Homepage reference
├── about.html                ← About page reference
├── contact.html              ← Contact page reference
├── case-studies.html         ← Case studies page reference
└── services/
    ├── ai-agents.html        ← AI Agent Development
    ├── automation.html       ← AI Automation & Workflows
    ├── saas.html             ← SaaS Product Development
    ├── software.html         ← Custom Software Development
    ├── websites.html         ← Website & Web App Development
    └── consulting.html       ← AI & Automation Consulting
```

Each HTML file contains the full content, copy, section structure, and design reference for that page. Use these as your blueprint when building in Elementor.
