# Dr. Nazif Mahbub — Portfolio

A polished, fully responsive personal portfolio for **Dr. Nazif Mahbub** (MBBS, MPH, CHE, FRSPH) — physician-turned-policy-analyst, personal-development advocate, and host of the Active Action Podcast.

Built as a plain static site (HTML, CSS, vanilla JS) — **no build step required** to deploy.

## Pages

| File | Page |
| --- | --- |
| `index.html` | Home — hero, credentials, animated stats, intro, featured services |
| `about.html` | About — full bio, education, credentials, career timeline |
| `services.html` | Services overview |
| `service-personal-development.html` | Personal Development Coaching → activeactionlab.com/transformyourself |
| `service-job-readiness.html` | Job Readiness Program → activeactionlab.com/jobready |
| `service-corporate-training.html` | Corporate Training Workshops → activeactionlab.com/corporatetraining |
| `service-mph-admission.html` | MPH Admission Coaching → activeactionlab.com/mph |
| `service-podcast-production.html` | Podcast Production (Pod Mechanic) → podmechanic.com |
| `contact.html` | Contact form → dr.nazif.mahbub@gmail.com |

Each service has its **own page** and links out to its detailed page on Active Action Lab, exactly as requested.

---

## 1. Add the headshot

The site references `assets/img/dr-nazif-headshot.jpg`. Drop the photo into
`assets/img/` with that exact filename and it appears automatically on the Home
and About pages. Until then a tidy placeholder shows where it goes. A portrait
(≈4:5) image around 1000×1250 px or larger looks best.

---

## 2. Make the contact form deliver to the inbox (one-time, ~2 min)

GitHub Pages is static, so it can't send email by itself. The form is wired for
[**Formspree**](https://formspree.io) (free tier), and falls back to opening the
visitor's email app if Formspree isn't set up yet — so it works either way.

To enable seamless, on-page sending:

1. Sign up at <https://formspree.io> using **dr.nazif.mahbub@gmail.com**.
2. Create a new form and confirm the email. Copy your form's endpoint, which
   looks like `https://formspree.io/f/abcdwxyz`.
3. Open `contact.html`, find this line:
   ```html
   <form id="contactForm" action="https://formspree.io/f/YOUR_FORM_ID" method="POST" novalidate>
   ```
   and replace `YOUR_FORM_ID` with your real ID (e.g. `.../f/abcdwxyz`).

That's it — submissions now arrive at dr.nazif.mahbub@gmail.com with a success
message shown in place, no page reload.

> **Not ready to use Formspree?** Leave the line as-is. The form will instead
> open the visitor's mail app pre-filled to dr.nazif.mahbub@gmail.com when they
> submit. No setup needed.

---

## 3. Deploy to GitHub Pages

### Option A — simplest (branch deploy)

1. Create a repo (e.g. `drnazif1`) and push these files to the `main` branch:
   ```bash
   git init
   git add .
   git commit -m "Portfolio site"
   git branch -M main
   git remote add origin https://github.com/<your-username>/drnazif1.git
   git push -u origin main
   ```
2. On GitHub: **Settings → Pages**.
3. Under **Build and deployment → Source**, choose **Deploy from a branch**.
4. Branch: **main**, folder: **/ (root)**. Save.
5. Wait ~1 minute. Your site goes live at
   `https://<your-username>.github.io/drnazif1/`.

### Option B — automated (GitHub Actions)

A workflow is included at `.github/workflows/deploy.yml`. After pushing to
`main`, go to **Settings → Pages → Source → GitHub Actions**. Every push then
deploys automatically.

All links and asset paths are **relative**, so the site works correctly whether
it's served from a project subpath (`/drnazif1/`) or a custom domain.

---

## Editing content

Page content is generated from a single script, `build.py`, which keeps the
shared navigation and footer consistent across all nine pages. To change
copy, services, the timeline, or stats:

1. Edit `build.py`.
2. Run `python3 build.py` to regenerate the HTML files.

You can also just edit the `.html` files directly if you prefer — they're plain
HTML. `build.py` is a convenience, not a requirement for the site to run.

---

## Tech notes

- Fonts: **Fraunces** (display) + **Hanken Grotesk** (body), via Google Fonts.
- No frameworks, no dependencies, no bundler — just open `index.html`.
- Accessible: keyboard-friendly nav, reduced-motion support, semantic markup.
- Performance: a single small CSS file and a single small JS file.
