# Key's Touch Website — WordPress Implementation (Step-by-Step)

This guide takes you from a fresh WordPress install to a fully live, branded, SEO-optimized version of your website. Every HTML file in this repo is your content/design blueprint.

---

## PHASE 1: WordPress Setup (30 minutes)

### Step 1: Log into WordPress
1. Go to `keystouch.com/wp-admin`
2. Log in with your admin credentials
3. You should see the WordPress Dashboard

### Step 2: Install the Theme — Kadence
1. Go to **Appearance > Themes > Add New**
2. Search for **"Kadence"**
3. Click **Install**, then **Activate**
4. You'll see a prompt to install **Kadence Starter Templates** — skip this for now
5. Optional: Purchase **Kadence Pro** ($79/year) for the header/footer builder — highly recommended but not required for initial launch

### Step 3: Install the Page Builder — Elementor Pro
1. Go to **Plugins > Add New**
2. Search for **"Elementor"** — install and activate the FREE version first
3. Purchase **Elementor Pro** ($59/year) at elementor.com
4. Download the Pro plugin zip from your Elementor account
5. Go to **Plugins > Add New > Upload Plugin** — upload the zip
6. Activate and connect your license

### Step 4: Install Required Plugins
Go to **Plugins > Add New** and install each:

| Plugin | How to Find | Purpose |
|--------|-------------|---------|
| **RankMath SEO** | Search "Rank Math" | SEO titles, schema, sitemaps |
| **WP Rocket** | Upload from wp-rocket.me ($59/yr) | Speed/caching |
| **WPForms Lite** | Search "WPForms" | Contact form (upgrade to Pro later) |
| **UpdraftPlus** | Search "UpdraftPlus" | Backups |
| **Redirection** | Search "Redirection" | 301 redirects from old URLs |
| **ShortPixel** | Search "ShortPixel" | Image compression/WebP |
| **Site Kit by Google** | Search "Site Kit" | GA4 analytics |

Activate all plugins after installing.

---

## PHASE 2: Global Settings (45 minutes)

### Step 5: Set Up Colors & Typography
1. Go to **Appearance > Customize > Colors & Fonts**
2. Set your global colors:
   ```
   Background:       #0A0A0A
   Surface/Cards:    #111113
   Primary (Cyan):   #00B4D8
   Secondary (Purple): #7C3AED
   Text:             #FFFFFF
   Subtle Text:      #B0B0C0
   Muted Text:       #6B6B80
   ```
3. Set your fonts:
   - **Headings:** Space Grotesk (Weight: 600-700)
   - **Body:** Inter (Weight: 400-500)
   - **Base size:** 16px

### Step 6: Upload Your Logo
1. Go to **Appearance > Customize > Header**
2. Upload `images/logo.png` from this repo
3. Set logo width to ~40px
4. Set site title to "Key's Touch"
5. Enable "Display Logo + Site Title" side by side

### Step 7: Set Up the Navigation Menu
1. Go to **Appearance > Menus**
2. Create a new menu called "Main Navigation"
3. Add these pages (create them as empty pages first if needed):
   - Services (dropdown with all 6 service pages)
   - Results (link to homepage #proof section)
   - Case Studies
   - About
4. Add a **Custom Link** for the CTA button:
   - URL: `/contact`
   - Label: `Free Automation Audit`
   - Add CSS class: `nav-cta` (enable CSS classes in Screen Options)
5. Assign to "Primary Menu" location

### Step 8: Configure Elementor Defaults
1. Go to **Elementor > Settings > Style**
2. Set default colors to match your palette
3. Set default fonts: Space Grotesk for headings, Inter for body
4. Set content width: 1200px
5. Set default padding for sections: 120px top/bottom (desktop)

---

## PHASE 3: Build the Pages (2-3 hours per page)

**IMPORTANT:** For each page, open the corresponding HTML file from this repo side-by-side with Elementor. The HTML file is your exact content + design reference.

### Step 9: Build the Homepage (`index.html`)
1. Go to **Pages > Add New**
2. Title: "Home"
3. Click **"Edit with Elementor"**
4. Build each section from `index.html`:

**Section 1: Hero (Split Layout)**
- Add a 2-column section (60/40 split)
- Left column: Heading (H1) + Text + 2 Buttons
- Right column: Use Elementor's Code Highlight or HTML widget for the terminal animation
- Copy the exact headline: "AI that replaces the busywork."
- Copy the exact body text from the HTML file
- Buttons: "Get a free automation audit" (primary) + "What we do" (ghost)
- Background: `#0A0A0A`
- Add CSS gradient orbs using Custom CSS (Elementor Pro feature)

**Section 2: Tech Partner Marquee**
- Use a **Marquee/Ticker widget** (Elementor Pro) or the **Unlimited Elements** plugin
- Add all partner names: OpenAI, Anthropic Claude, AWS, LangChain, n8n, Make, etc.
- Set to auto-scroll

**Section 3: Metrics Counter Strip**
- 4-column section with Counter widgets
- Values: 500+, 4.2x, 73%, 98%
- Dark background with border

**Section 4: RAPID Framework**
- 2-column layout
- Left: heading + description text
- Right: 5 lettered steps (R-A-P-I-D) with descriptions
- Use Icon List or custom layout

**Section 5: Services (Numbered List)**
- Use Elementor's Toggle or Accordion widget, OR
- Build as repeating rows with number, title, description, and tag pills
- Copy all 6 services with exact text from the HTML file

**Section 6: Big Quote Testimonial**
- Full-width centered section
- Large quote mark (Georgia font, cyan color, low opacity)
- Quote text in Space Grotesk, large size
- Author name below

**Section 7: ROI Calculator**
- Use Elementor's HTML widget to embed the calculator JavaScript from `index.html`
- Copy the entire `<div class="calculator">` block and its associated `<script>` code
- Style the container to match

**Section 8: Process (How It Works)**
- 2-column: left text + CTA, right numbered steps
- Copy exact text from the HTML file

**Section 9: Why Key's Touch**
- 3-column cards with cyan headings
- Copy the 3 differentiators

**Section 10: Second Testimonial**
- Simpler quote, smaller font than the first

**Section 11: Bottom CTA**
- Dark background with centered text
- "The audit is free. The call is 30 minutes. The ROI speaks for itself."
- Button: "Book the free audit"

5. Set this page as your **Static Homepage**: Settings > Reading > Static page > Home

### Step 10: Build Service Pages
For each service page, follow the same process:
1. Create a new page
2. Edit with Elementor
3. Reference the corresponding HTML file in `/services/`
4. Use the same section patterns: Hero > Services Grid > Process > Tech Stack > Case Study Link > CTA

**Pages to create:**
- AI Agent Development (`services/ai-agents.html`)
- AI Automation & Workflows (`services/automation.html`)
- SaaS Product Development (`services/saas.html`)
- Custom Software Development (`services/software.html`)
- Website & Web App Development (`services/websites.html`)
- AI & Automation Consulting (`services/consulting.html`)

**Pro tip:** Build the first service page, then save it as an **Elementor Template**. Duplicate it for the other 5 and just swap the content.

### Step 11: Build the About Page (`about.html`)
- Hero: "We build it. You own it."
- Tech partner marquee (same as homepage)
- By the Numbers counter strip
- RAPID Framework section
- "What you won't get from us" cards
- Founder section with PMP/AI governance credentials
- CTA

### Step 12: Build the Case Studies Page (`case-studies.html`)
- Hero: "The receipts."
- Filter bar (use Elementor tabs or buttons — can be visual-only for now)
- 4 case study cards with Problem/Built/Results format
- Each card includes tech stack tags and RAPID phase tags
- Bottom CTA: "Want to be the next case study?"

### Step 13: Build the Contact Page (`contact.html`)
- Hero: "Let's talk."
- 2-column layout: form + info cards
- Left: Calendly embed + WPForms contact form
- Right: "What happens next" (RAPID step 1), contact info, FAQs
- "Not ready to talk?" section with 3 link cards

**Calendly Setup:**
1. Create a free account at calendly.com
2. Create a 30-minute event type called "Free Automation Audit"
3. Get your embed code from Calendly > Share > Embed
4. Paste into an Elementor HTML widget where the placeholder is

**WPForms Setup:**
1. Go to WPForms > Add New
2. Create a form with: First Name, Last Name, Email, Company, Service Interest (dropdown), Message
3. Set notifications to go to `hello@keystouch.com`
4. Embed in the contact page using the WPForms widget

---

## PHASE 4: Chat Widget & Automations (30 minutes)

### Step 14: Add the Chat Widget
**Option A: Custom (from your HTML)**
1. Go to **Appearance > Customize > Additional CSS**
2. Paste the chat widget CSS from `index.html`
3. Go to **Appearance > Customize > Custom Scripts** (Kadence Pro) OR install **Insert Headers and Footers** plugin
4. Paste the chat widget HTML + JavaScript into the footer scripts
5. This will appear on every page

**Option B: Use Tidio or Crisp (easier, more features)**
1. Sign up at tidio.com (free plan available)
2. Set up a chatbot flow matching the 4 options from your HTML:
   - "I want to automate something specific" → link to /contact
   - "I need software or an app built" → link to /contact
   - "I want to add AI to my business" → link to /services/consulting
   - "Just browsing" → link to /case-studies
3. Install the Tidio WordPress plugin
4. Configure trigger: auto-open after 30 seconds

### Step 15: Add the Exit-Intent Popup
**Option A: Custom (from your HTML)**
- Same process as chat widget — paste CSS, HTML, and JS into footer scripts

**Option B: Use OptinMonster or ConvertKit (recommended)**
1. Sign up at optinmonster.com or convertkit.com
2. Create an exit-intent popup:
   - Headline: "Before you go —"
   - Body: 'Get our free guide: "10 Workflows Every Business Should Automate in 2026."'
   - Email capture field
3. Set trigger: Exit Intent (desktop), Scroll 80% (mobile)
4. Connect to your email service for the nurture sequence
5. Install the WordPress plugin

### Step 16: Add the ROI Calculator
1. Create a **Custom HTML** widget in Elementor on the homepage
2. Paste the calculator HTML from `index.html` (the `<div class="calculator">` block)
3. Add the JavaScript in a separate HTML widget below it
4. Test that sliders update the annual number correctly

---

## PHASE 5: SEO Setup (30 minutes)

### Step 17: Configure RankMath
1. Go to **Rank Math > Dashboard > Setup Wizard**
2. Run through the wizard:
   - Site type: Small Business
   - Business name: Key's Touch
   - Logo: Upload your logo
3. Go to **Rank Math > Titles & Meta**:
   - Homepage title: `Key's Touch | AI Automation & Software Consulting Agency`
   - Homepage description: (copy from index.html meta description)
4. Enable **Schema Markup** in RankMath:
   - Default type: Organization
   - Add Local Business schema
5. For each page, click **Edit Snippet** in the RankMath meta box:
   - Set the SEO title and description from each HTML file's `<title>` and `<meta name="description">`
   - Set the canonical URL
   - Add Open Graph image

### Step 18: Add Schema Markup
RankMath handles basic schema. For the advanced schema (FAQPage on Contact, Service schema on service pages):
1. Go to each page in the editor
2. Open the RankMath sidebar > Schema tab
3. Add the appropriate schema type
4. Fill in the fields matching the JSON-LD from each HTML file

### Step 19: Create XML Sitemap
1. Go to **Rank Math > Sitemap Settings**
2. Enable the sitemap
3. Verify at `keystouch.com/sitemap_index.xml`
4. Submit to Google Search Console (see Phase 7)

---

## PHASE 6: Speed Optimization (20 minutes)

### Step 20: Configure WP Rocket
1. Go to **Settings > WP Rocket**
2. Enable:
   - Page Caching: ON
   - Browser Caching: ON
   - Minify CSS: ON
   - Minify JavaScript: ON
   - Defer JavaScript: ON
   - Lazy Load Images: ON
3. Under CDN tab: Enable if using Cloudflare

### Step 21: Set Up Cloudflare (Free)
1. Sign up at cloudflare.com
2. Add your domain `keystouch.com`
3. Change nameservers at your domain registrar to Cloudflare's
4. Enable:
   - SSL: Full (Strict)
   - Auto Minify: HTML, CSS, JS
   - Brotli compression: ON
   - Always Use HTTPS: ON
5. Set Page Rules:
   - `keystouch.com/wp-admin/*` → Cache Level: Bypass

### Step 22: Optimize Images
1. Go to **Settings > ShortPixel**
2. Get a free API key from shortpixel.com
3. Enable WebP conversion
4. Bulk optimize existing images
5. Set compression level: Lossy (best for web)

---

## PHASE 7: Analytics & Tracking (20 minutes)

### Step 23: Set Up Google Analytics 4
1. Go to analytics.google.com
2. Create a new GA4 property for keystouch.com
3. In WordPress: Go to **Site Kit > Setup**
4. Connect your Google account
5. Site Kit will automatically add the GA4 tracking code

### Step 24: Set Up Microsoft Clarity (Heatmaps)
1. Go to clarity.microsoft.com
2. Create a new project for keystouch.com
3. Get the tracking code
4. In WordPress: Go to **Appearance > Customize > Custom Scripts** (or Insert Headers and Footers plugin)
5. Paste the Clarity code in the `<head>` section

### Step 25: Set Up Conversion Tracking
In GA4, create these events:
1. `form_submit` — fires when contact form is submitted
2. `calendly_booking` — fires when Calendly appointment is booked
3. `cta_click` — fires when any CTA button is clicked
4. `calculator_used` — fires when ROI calculator is interacted with
5. `chat_engaged` — fires when chat widget option is clicked

---

## PHASE 8: Redirects & Go-Live (15 minutes)

### Step 26: Set Up 301 Redirects
Your old site had different URL structures. Set up redirects so no links break:

1. Go to **Tools > Redirection**
2. Add these redirects:

| Old URL | New URL |
|---------|---------|
| `/product` | `/case-studies` |
| `/about-us` | `/about` |
| Any old service URLs | New service page URLs |

### Step 27: Pre-Launch Checklist
Go through each item:

- [ ] All 10 pages built and reviewed
- [ ] Mobile responsive (test on real phone)
- [ ] Contact form tested — submissions received
- [ ] Calendly embed working — can book appointments
- [ ] Chat widget showing and interactive
- [ ] ROI calculator functional
- [ ] Exit-intent popup triggers on desktop
- [ ] All nav links working (including anchor links to homepage sections)
- [ ] Footer links working
- [ ] SEO titles and descriptions set for all pages
- [ ] Schema markup validated (search.google.com/test/rich-results)
- [ ] PageSpeed score 85+ on mobile (pagespeed.web.dev)
- [ ] SSL working (HTTPS, green padlock)
- [ ] Favicon uploaded
- [ ] OG images uploaded for social sharing
- [ ] XML sitemap accessible
- [ ] Old URLs redirecting properly
- [ ] Backup configured (UpdraftPlus)
- [ ] WP Rocket caching active

### Step 28: Submit to Google
1. Go to search.google.com/search-console
2. Add property: `keystouch.com`
3. Verify ownership (DNS or HTML file method)
4. Submit your sitemap: `keystouch.com/sitemap_index.xml`
5. Request indexing for your homepage

---

## PHASE 9: Post-Launch (First 30 Days)

### Week 1
- Monitor GA4 for traffic and conversions
- Check Clarity heatmaps — are people clicking CTAs?
- Fix any broken links or display issues
- Test all forms and bookings one more time

### Week 2
- Review Clarity recordings — watch 10 real user sessions
- Adjust CTA placement based on heatmap data
- Check Google Search Console for crawl errors

### Week 3
- Publish first blog post (for SEO)
- Share site on LinkedIn
- Request indexing for all pages in Search Console

### Week 4
- Review conversion rates (form fills, bookings)
- A/B test homepage headline if traffic allows
- Apply to Clutch.co, GoodFirms, and G2 for reviews

---

## Quick Reference: Page → HTML File Mapping

| WordPress Page | HTML Reference File |
|---|---|
| Home | `index.html` |
| About | `about.html` |
| Contact | `contact.html` |
| Case Studies | `case-studies.html` |
| AI Agent Development | `services/ai-agents.html` |
| AI Automation & Workflows | `services/automation.html` |
| SaaS Product Development | `services/saas.html` |
| Custom Software Development | `services/software.html` |
| Website & Web App Development | `services/websites.html` |
| AI & Automation Consulting | `services/consulting.html` |

---

## Estimated Total Time

| Phase | Time |
|---|---|
| WordPress Setup | 30 min |
| Global Settings | 45 min |
| Build Pages (10 pages) | 15-25 hours |
| Chat & Automations | 30 min |
| SEO Setup | 30 min |
| Speed Optimization | 20 min |
| Analytics | 20 min |
| Redirects & Go-Live | 15 min |
| **Total** | **~20-28 hours** |

You can do this over a weekend if you're focused, or spread it across a week doing 2-3 pages per day.
