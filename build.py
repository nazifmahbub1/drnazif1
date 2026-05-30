# -*- coding: utf-8 -*-
"""Static-site generator for Dr. Nazif Mahbub's portfolio.
Emits plain HTML files (no runtime build step) for GitHub Pages."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))
HEADSHOT = "assets/img/dr-nazif-headshot.jpg"

# ---------------------------------------------------------------- icons
IC = {
"arrow":  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
"ext":    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>',
"chev":   '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>',
"target": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.2"/></svg>',
"brief":  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
"users":  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
"cap":    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10L12 5 2 10l10 5 10-5z"/><path d="M6 12v5c0 1 2.7 2.5 6 2.5s6-1.5 6-2.5v-5"/><line x1="22" y1="10" x2="22" y2="15"/></svg>',
"mic":    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 10a7 7 0 0 0 14 0"/><line x1="12" y1="17" x2="12" y2="22"/><line x1="8" y1="22" x2="16" y2="22"/></svg>',
"mail":   '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>',
"globe":  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15 15 0 0 1 0 20 15 15 0 0 1 0-20z"/></svg>',
"pin":    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
"play":   '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polygon points="10 8 16 12 10 16 10 8" fill="currentColor" stroke="none"/></svg>',
"user":   '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21v-1a7 7 0 0 1 14 0v1"/></svg>',
"check":  '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
}

# ---------------------------------------------------------------- services data
SERVICES = [
  {
    "key": "personal-development",
    "num": "01",
    "title": "Personal Development Coaching",
    "icon": "target",
    "card": "A four-week, one-to-one intensive that builds the mindset, habits, and skills for lasting change — with guided self-assessment, practical tools, and free access to the Transform Yourself course.",
    "lead": "The next step for someone ready to transform their life with clarity and confidence. A focused 1:1 program built around your goals — not generic motivation — so the change actually lasts.",
    "detail": "https://activeactionlab.com/transformyourself",
    "tags": ["4-week program", "1:1 intensive", "Includes free course"],
    "features": [
      "A structured four-week journey designed around your goals and your starting point",
      "Guided self-assessment to map where you are and where you want to be",
      "Evidence-based tools for mindset, habits, and self-leadership you can use immediately",
      "The clarity and confidence to navigate transitions and make hard decisions",
      "Complimentary access to the Transform Yourself online masterclass",
      "Honest accountability and feedback through every session",
    ],
    "meta": [("Format", "1:1 coaching"), ("Duration", "4 weeks"), ("Delivery", "Virtual"), ("Bonus", "Free course")],
  },
  {
    "key": "job-readiness",
    "num": "02",
    "title": "Job Readiness Program",
    "icon": "brief",
    "card": "A four-week, one-to-one intensive that turns your job search around — a resume that gets interviews, an optimised LinkedIn profile, compelling cover letters, and a portfolio that proves your capabilities.",
    "lead": "The next step for someone ready to get hired with materials that genuinely stand out. We build the assets and the strategy that set you up to win in a competitive market.",
    "detail": "https://activeactionlab.com/jobready",
    "tags": ["4-week program", "1:1 intensive", "Includes free course"],
    "features": [
      "A resume engineered to pass screening and get you interviews",
      "LinkedIn profile optimisation that makes recruiters reach out",
      "Compelling, tailored cover letters for the roles you actually want",
      "A portfolio that demonstrates your capabilities, not just lists them",
      "Interview preparation and a clear job-hunting strategy",
      "Complimentary access to the supporting online course",
    ],
    "meta": [("Format", "1:1 coaching"), ("Duration", "4 weeks"), ("Delivery", "Virtual"), ("Bonus", "Free course")],
  },
  {
    "key": "corporate-training",
    "num": "03",
    "title": "Corporate Training Workshops",
    "icon": "users",
    "card": "Interactive workshops that build the communication, leadership, and collaboration skills teams need to perform — delivered on-site, virtually, or hybrid, with tailored content and post-training resources.",
    "lead": "The next step for organisations ready to build stronger teams, sharper leaders, and a high-performing culture. Practical, interactive sessions designed around your people and your goals.",
    "detail": "https://activeactionlab.com/corporatetraining",
    "tags": ["On-site · virtual · hybrid", "Tailored content", "Resource kits"],
    "features": [
      "Workshops on communication, leadership, and collaboration tuned to your team",
      "Interactive, real-world exercises — not slideware lectures",
      "Content tailored to your industry, challenges, and objectives",
      "Flexible delivery: on-site, virtual, or hybrid",
      "Post-training resource kits so the learning sticks",
      "Follow-up coaching to embed new habits across the organisation",
    ],
    "meta": [("Audience", "Teams & leaders"), ("Delivery", "On-site / virtual / hybrid"), ("Format", "Interactive workshop"), ("Extras", "Resource kits + coaching")],
  },
  {
    "key": "mph-admission",
    "num": "04",
    "title": "MPH Admission Coaching",
    "icon": "cap",
    "card": "A focused intensive for aspiring public-health professionals — understand Canadian MPH admissions, build competitive application materials, and position yourself for acceptance. Spots are limited.",
    "lead": "The next step for aspiring public-health professionals ready to pursue MPH programs in Canada. Built and taught by someone who navigated the exact same path to the University of Alberta.",
    "detail": "https://activeactionlab.com/mph",
    "tags": ["4 sessions · 10 hours", "Canada-focused", "Limited spots"],
    "features": [
      "A clear map of how Canadian MPH admissions actually work",
      "Competitive application materials — statement, CV, and references",
      "Program-selection strategy matched to your profile and goals",
      "Positioning that helps you stand out to admissions committees",
      "Guidance grounded in real, first-hand experience of the journey",
      "Four focused sessions totalling roughly ten hours of coaching",
    ],
    "meta": [("Format", "Intensive coaching"), ("Structure", "4 sessions · ~10 hrs"), ("Focus", "Canadian MPH"), ("Availability", "Limited — book ahead")],
  },
  {
    "key": "podcast-production",
    "num": "05",
    "title": "Podcast Production — Pod Mechanic",
    "icon": "mic",
    "card": "A done-for-you podcast studio. You record; Pod Mechanic handles editing, cleanup, mixing, video, show notes, social clips, and distribution — so every episode sounds clean and ready to stream.",
    "lead": "Pod Mechanic is a done-for-you podcast production studio for independent creators, businesses, and nonprofits. You record — the team handles everything else, at an affordable cost.",
    "detail": "https://podmechanic.com/",
    "tags": ["Done-for-you", "Audio + video", "For brands & creators"],
    "features": [
      "Full episode editing, cleanup, and professional mixing",
      "Video editing for YouTube and social platforms",
      "Show notes written and formatted for every episode",
      "Short social clips to grow your audience between releases",
      "Launch support and distribution across podcast platforms",
      "Affordable plans for independent creators, businesses, and nonprofits",
    ],
    "meta": [("Model", "Done-for-you"), ("Covers", "Audio · video · notes"), ("Good for", "Creators & brands"), ("Studio", "Pod Mechanic")],
  },
]

CRED_FULL = [
  ("MBBS", "Bachelor of Medicine & Surgery", "University of Dhaka — trained and practised as a physician."),
  ("MPH", "Master of Public Health", "University of Alberta — Health Policy & Management."),
  ("CHE", "Certified Health Executive", "Canadian College of Health Leaders — LEADS leadership framework."),
  ("FRSPH", "Fellow, Royal Society for Public Health", "Recognised for contributions to public health and population well-being."),
]

# ---------------------------------------------------------------- shared chrome
def nav(active):
  def link(href, label, key):
    cls = ' class="active"' if key == active else ""
    return '<a href="%s"%s>%s</a>' % (href, cls, label)
  return """
<header class="nav" id="nav">
  <div class="wrap nav-inner">
    <a href="index.html" class="brand" aria-label="Dr. Nazif Mahbub — home">
      <span class="mark">NM</span>
      <span>Dr. Nazif Mahbub<small>Coach · Advocate · Host</small></span>
    </a>
    <button class="nav-toggle" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="nav-links" aria-label="Primary">
      %s
      %s
      %s
      %s
      <a href="contact.html" class="btn btn-accent nav-cta">Work with me %s</a>
    </nav>
  </div>
</header>
""" % (
    link("index.html", "Home", "home"),
    link("about.html", "About", "about"),
    link("services.html", "Services", "services"),
    link("contact.html", "Contact", "contact"),
    IC["arrow"],
  )

def footer():
  svc_links = "".join('<a href="service-%s.html">%s</a>' % (s["key"], s["title"].split(" — ")[0]) for s in SERVICES)
  return """
<footer class="footer">
  <div class="wrap">
    <div class="footer-top">
      <div>
        <a href="index.html" class="brand"><span class="mark">NM</span><span>Dr. Nazif Mahbub</span></a>
        <p>Physician by training, policy analyst by profession, and a personal-development advocate helping people build the clarity, confidence, and skills to transform their lives.</p>
      </div>
      <div class="footer-col">
        <h5>Explore</h5>
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
        <a href="services.html">Services</a>
        <a href="contact.html">Contact</a>
      </div>
      <div class="footer-col">
        <h5>Services</h5>
        %s
      </div>
      <div class="footer-col">
        <h5>Elsewhere</h5>
        <a href="https://activeactionlab.com" target="_blank" rel="noopener">Active Action Lab %s</a>
        <a href="https://activeactionlab.com/podcast" target="_blank" rel="noopener">Active Action Podcast %s</a>
        <a href="https://podmechanic.com" target="_blank" rel="noopener">Pod Mechanic %s</a>
        <a href="mailto:dr.nazif.mahbub@gmail.com">dr.nazif.mahbub@gmail.com</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span id="year">2026</span> Dr. Nazif Mahbub. All rights reserved.</span>
      <span>Built with care · <a href="contact.html">Get in touch</a></span>
    </div>
  </div>
</footer>
""" % (svc_links, IC["ext"], IC["ext"], IC["ext"])

def page(title, desc, active, body, extra_head=""):
  return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
<meta name="description" content="%s">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..600;1,9..144,400..600&family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
<link rel="icon" href="data:image/svg+xml,%%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%%3E%%3Crect width='100' height='100' rx='22' fill='%%231C2B24'/%%3E%%3Ctext x='50' y='66' font-family='Georgia,serif' font-size='46' fill='%%23F6F1E7' text-anchor='middle'%%3ENM%%3C/text%%3E%%3C/svg%%3E">
%s
</head>
<body>
%s
%s
%s
<script src="assets/js/main.js"></script>
</body>
</html>""" % (title, desc, extra_head, nav(active), body, footer())

def portrait(extra_class=""):
  return """
  <div class="portrait %s">
    <img src="%s" alt="Dr. Nazif Mahbub" onerror="this.closest('.portrait').classList.add('noimg');this.remove();">
    <div class="ph">
      <div>%s
        <small>Add the headshot at<br><code>%s</code></small>
      </div>
    </div>
  </div>""" % (extra_class, HEADSHOT, IC["user"], HEADSHOT)

# ---------------------------------------------------------------- HOME
def home():
  creds = "".join('<span class="cred-chip">%s</span>' % c for c in ["MBBS", "MPH", "CHE", "FRSPH"])
  stats = [
    ("45", "K+", "Community members"),
    ("15", "+", "Countries reached"),
    ("20", "K+", "Podcast downloads"),
    ("50", "+", "Episodes published"),
  ]
  stat_html = "".join(
    '<div class="stat"><div class="num" data-count="%s" data-suffix="%s">%s<span>%s</span></div><div class="lbl">%s</div></div>'
    % (n, suf, n, suf, lbl) for n, suf, lbl in stats)
  svc_cards = ""
  for s in SERVICES[:3]:
    svc_cards += """
      <a class="svc-card" href="service-%s.html" data-reveal data-reveal-delay="%s">
        <span class="svc-num">%s</span>
        <span class="svc-icon">%s</span>
        <h3>%s</h3>
        <p>%s</p>
        <span class="svc-link">Explore %s</span>
      </a>""" % (s["key"], SERVICES.index(s)+1, s["num"], IC[s["icon"]], s["title"].split(" — ")[0], s["card"], IC["arrow"])

  body = """
<section class="hero">
  <div class="wrap">
    <div class="hero-grid">
      <div class="hero-copy">
        <span class="kicker">Stay Active · Take Action</span>
        <h1 class="display">Helping people build the <em>clarity, confidence &amp; skills</em> to transform their lives.</h1>
        <div class="hero-creds">%s</div>
        <p class="hero-lead">I'm Dr. Nazif Mahbub — a former physician, public-health policy analyst, and personal-development advocate. Through coaching, training, and the Active Action Podcast, I turn lived experience into practical tools for real growth.</p>
        <div class="hero-actions">
          <a href="services.html" class="btn btn-primary">Explore services %s</a>
          <a href="about.html" class="btn btn-ghost">My story</a>
        </div>
      </div>
      <div class="portrait-wrap">
        <svg class="portrait-arc" viewBox="0 0 400 400" fill="none" aria-hidden="true"><path d="M200 20a180 180 0 0 1 0 360" stroke="%%23BE6A38" stroke-width="2" stroke-dasharray="3 10" opacity=".5"/></svg>
        %s
        <div class="portrait-badge"><span class="dot"></span><div><b>Active Action Lab</b><span>Founder &amp; Host</span></div></div>
      </div>
    </div>
    <div class="stats" data-reveal>%s</div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <span class="kicker">Why this work</span>
    <p class="quote-lead">Real growth doesn't come from inspiration. It comes from <em>action</em> — honest conversations, practical tools, and one focused step at a time.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="kicker">What I do</span>
      <h2 class="display">Coaching and programs built on lived experience</h2>
      <p>From one-to-one coaching to corporate workshops and full podcast production — each service is designed to create lasting, measurable change.</p>
    </div>
    <div class="svc-grid">%s</div>
    <div style="margin-top:34px" data-reveal>
      <a href="services.html" class="btn btn-ghost">See all five services %s</a>
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="cta" data-reveal>
      <h2 class="display">Ready to take action?</h2>
      <p>Whether you're growing your career, leading a team, or launching a podcast — let's build a plan that actually moves you forward.</p>
      <a href="contact.html" class="btn btn-accent">Start a conversation %s</a>
    </div>
  </div>
</section>
""" % (creds, IC["arrow"], portrait(), stat_html, svc_cards, IC["arrow"], IC["arrow"])
  return page(
    "Dr. Nazif Mahbub — Coach, Advocate &amp; Podcast Host",
    "Dr. Nazif Mahbub (MBBS, MPH, CHE, FRSPH) — former physician, public-health policy analyst, and personal-development advocate. Coaching, corporate training, MPH admission guidance, and podcast production.",
    "home", body)

# ---------------------------------------------------------------- ABOUT
def about():
  cred_boxes = "".join(
    '<div class="cred-box" data-reveal data-reveal-delay="%s"><div class="ab">%s</div><h4>%s</h4><p>%s</p></div>'
    % (i+1, ab, full, note) for i, (ab, full, note) in enumerate(CRED_FULL))

  timeline = [
    ("Dhaka, Bangladesh", "Trained as a physician",
     "Earned an MBBS from the University of Dhaka and began practising medicine — while sensing he was drawn to the bigger picture: the systems, policies, and social factors that decide who stays healthy."),
    ("The leap", "Immigrated to Canada",
     "Navigated the Federal Skilled Worker pathway — one of Canada's most competitive immigration programs — and started over in a new country, proving himself all over again."),
    ("University of Alberta", "Master of Public Health",
     "Completed an MPH specialising in Health Policy & Management while working as a Graduate Research Assistant and as a Research & Policy Analyst at a Canadian non-profit (CRIDA)."),
    ("Giving back", "Co-founded community organisations",
     "Co-founded Active Action Organization to help newcomers integrate into Canada, and serves as a Board Member and Advisor of One Better World in Bangladesh."),
    ("Leadership credentials", "CHE & FRSPH",
     "Earned the Certified Health Executive (CHE) designation from the Canadian College of Health Leaders and became a Fellow of the Royal Society for Public Health (FRSPH)."),
    ("Government of Alberta", "Policy Analyst",
     "Supports the Ministry in regulating health professionals and developing evidence-based policy across Health Workforce, Continuing Care, Social Services, and Mental Health & Addiction."),
    ("Active Action Lab", "Founder, coach & podcast host",
     "Founded Active Action Lab and launched the Active Action Podcast — now 15,000+ followers and 20,000+ downloads — alongside the Transform Yourself program, corporate training, and the free Life Skill School."),
  ]
  tl_html = "".join(
    '<div class="tl-item" data-reveal><div class="tl-when">%s</div><h4>%s</h4><p>%s</p></div>'
    % (w, t, d) for w, t, d in timeline)

  body = """
<section class="about-hero">
  <div class="wrap">
    <div class="section-head" data-reveal style="max-width:760px">
      <span class="kicker">About</span>
      <h2 class="display" style="font-size:clamp(2.3rem,5vw,3.7rem)">From a physician in Dhaka to a personal-development advocate in Canada.</h2>
      <p>Dr. Nazif doesn't coach from textbook theory — he coaches from lived experience. This is the journey behind the work.</p>
    </div>
    <div class="about-grid">
      <aside class="about-figure" data-reveal>
        %s
        <div class="figure-card">
          <h4>At a glance</h4>
          <ul class="figure-list">
            <li>%s<span>Policy Analyst, Government of Alberta</span></li>
            <li>%s<span>Founder &amp; Host, Active Action Lab</span></li>
            <li>%s<span>Based in Alberta, Canada</span></li>
            <li>%s<span>Co-founder, Active Action Organization</span></li>
          </ul>
        </div>
      </aside>
      <div class="prose">
        <p data-reveal>Dr. Nazif Mahbub's journey didn't begin as a coach or a podcaster. It started in Dhaka, Bangladesh, where a young medical student was questioning whether the traditional path laid out before him was the only way forward.</p>
        <p data-reveal>After earning his <strong>MBBS from the University of Dhaka</strong> and working as a physician, he could have settled into a stable, predictable career. But he had always been drawn to the bigger picture — not just treating individual patients, but understanding the systems, policies, and social factors that determine who gets sick and who stays healthy in the first place.</p>

        <h3 data-reveal>Starting over in a new country</h3>
        <p data-reveal>Immigrating to Canada wasn't just a dream — it was a rigorous, competitive process. Dr. Nazif successfully navigated the <strong>Federal Skilled Worker pathway</strong>, demonstrating the qualifications, experience, and language proficiency that only the most competitive applicants achieve. Arriving meant leaving behind family, familiarity, and the security of his medical degree — and proving himself all over again.</p>
        <p data-reveal>He enrolled in the <strong>Master of Public Health program at the University of Alberta</strong>, specialising in Health Policy &amp; Management, working throughout as a Graduate Research Assistant and as a Research &amp; Policy Analyst at a Canadian non-profit.</p>

        <h3 data-reveal>Turning challenge into impact</h3>
        <p data-reveal>Like many newcomers, he faced uncertainty, the struggle to translate credentials across borders, and the pressure of proving himself in unfamiliar systems. Instead of letting those challenges break him, he used them as fuel — co-founding <strong>Active Action Organization</strong> to help other newcomers, and serving as a Board Member and Advisor of <strong>One Better World</strong> in Bangladesh.</p>
        <p data-reveal>While working full-time in public service, he pursued the <strong>Certified Health Executive (CHE)</strong> designation — mastering the LEADS framework through leadership assessments, real-world projects, and a comprehensive exam — and became a <strong>Fellow of the Royal Society for Public Health (FRSPH)</strong>, all while serving as a <strong>Policy Analyst at the Government of Alberta</strong>.</p>

        <h3 data-reveal>Finding his calling</h3>
        <p data-reveal>Along the way, Dr. Nazif realised that the very skills that helped him navigate his own journey — resilience, adaptability, clear communication, self-leadership, and goal-setting — were exactly what others were struggling with. So he founded <strong>Active Action Lab</strong> and launched the <strong>Active Action Podcast</strong>, which grew to over 15,000 followers and 20,000+ downloads.</p>
        <p data-reveal>Believing that personal development shouldn't be a luxury, he also created the free <strong>Life Skill School</strong> — hundreds of strategy guides, tutorials, and tools — democratising growth for anyone willing to put in the work. His mission is simple: help you build the clarity, confidence, and skills to transform your life, one honest conversation and one focused action at a time.</p>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="kicker">Education &amp; credentials</span>
      <h2 class="display">Trained across medicine, public health &amp; leadership</h2>
    </div>
    <div class="cred-grid">%s</div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head" data-reveal>
      <span class="kicker">Career timeline</span>
      <h2 class="display">The path so far</h2>
    </div>
    <div class="timeline">%s</div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="cta" data-reveal>
      <h2 class="display">Let's build your next chapter</h2>
      <p>If any part of this story resonates, there's probably a way I can help. Let's talk about where you want to go.</p>
      <a href="contact.html" class="btn btn-accent">Get in touch %s</a>
    </div>
  </div>
</section>
""" % (portrait(), IC["brief"], IC["mic"], IC["pin"], IC["users"], cred_boxes, tl_html, IC["arrow"])
  return page(
    "About — Dr. Nazif Mahbub",
    "The story of Dr. Nazif Mahbub — from physician in Dhaka to public-health policy analyst and personal-development advocate in Canada. Education, credentials (MBBS, MPH, CHE, FRSPH), and career timeline.",
    "about", body)

# ---------------------------------------------------------------- SERVICES OVERVIEW
def services_index():
  cards = ""
  for i, s in enumerate(SERVICES):
    cards += """
      <a class="svc-card" href="service-%s.html" data-reveal data-reveal-delay="%s">
        <span class="svc-num">%s</span>
        <span class="svc-icon">%s</span>
        <h3>%s</h3>
        <p>%s</p>
        <span class="svc-link">Learn more %s</span>
      </a>""" % (s["key"], (i % 4) + 1, s["num"], IC[s["icon"]], s["title"].split(" — ")[0], s["card"], IC["arrow"])
  body = """
<section class="about-hero">
  <div class="wrap">
    <div class="section-head" data-reveal style="max-width:720px">
      <span class="kicker">Services</span>
      <h2 class="display" style="font-size:clamp(2.3rem,5vw,3.7rem)">Five ways to grow — for individuals, teams &amp; creators</h2>
      <p>Each service has its own page with the full details, and a direct link through to book or read more on Active Action Lab.</p>
    </div>
    <div class="svc-grid">%s</div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="cta" data-reveal>
      <h2 class="display">Not sure which is right for you?</h2>
      <p>Tell me a little about your goals and I'll point you to the best fit — or build something tailored.</p>
      <a href="contact.html" class="btn btn-accent">Ask a question %s</a>
    </div>
  </div>
</section>
""" % (cards, IC["arrow"])
  return page(
    "Services — Dr. Nazif Mahbub",
    "Services by Dr. Nazif Mahbub: personal development coaching, job readiness, corporate training workshops, MPH admission coaching, and podcast production with Pod Mechanic.",
    "services", body)

# ---------------------------------------------------------------- SERVICE DETAIL
def service_detail(s):
  pills = ""
  for o in SERVICES:
    cls = ' class="active"' if o["key"] == s["key"] else ""
    pills += '<a href="service-%s.html"%s>%s</a>' % (o["key"], cls, o["title"].split(" — ")[0])
  tags = "".join("<span>%s</span>" % t for t in s["tags"])
  feats = "".join("<li>%s</li>" % f for f in s["features"])
  meta = "".join("<div><span>%s</span><span>%s</span></div>" % (k, v) for k, v in s["meta"])
  title_plain = s["title"].split(" — ")[0]

  body = """
<section class="svc-hero">
  <div class="wrap">
    <div class="crumbs">
      <a href="index.html">Home</a> %s
      <a href="services.html">Services</a> %s
      <span>%s</span>
    </div>
    <div class="svc-hero-grid">
      <div data-reveal>
        <span class="kicker">Service %s</span>
        <h1 class="display">%s</h1>
        <p class="lead">%s</p>
        <div class="svc-tag">%s</div>
      </div>
      <div class="svc-emblem" data-reveal data-reveal-delay="2">%s</div>
    </div>
  </div>
</section>

<section style="padding-top:30px">
  <div class="wrap">
    <div class="svc-body">
      <div data-reveal>
        <span class="kicker">What's included</span>
        <h2 class="display" style="font-size:clamp(1.7rem,3.4vw,2.4rem);margin:16px 0 8px">Everything you get</h2>
        <ul class="feature-list">%s</ul>
      </div>
      <aside class="svc-aside" data-reveal data-reveal-delay="1">
        <h4>%s</h4>
        <p>Read the full breakdown, pricing, and booking options on Active Action Lab.</p>
        <div class="meta">%s</div>
        <a href="%s" target="_blank" rel="noopener" class="btn btn-accent">View full details %s</a>
        <a href="contact.html" class="btn btn-ghost">Ask Dr. Nazif</a>
      </aside>
    </div>
    <div style="margin-top:60px" data-reveal>
      <span class="kicker">Other services</span>
      <div class="svc-pills">%s</div>
    </div>
  </div>
</section>

<section style="padding-top:30px">
  <div class="wrap">
    <div class="cta" data-reveal>
      <h2 class="display">Interested in %s?</h2>
      <p>Get the complete details on Active Action Lab, or reach out directly and we'll find the right starting point.</p>
      <a href="%s" target="_blank" rel="noopener" class="btn btn-accent">Read more on Active Action Lab %s</a>
    </div>
  </div>
</section>
""" % (IC["chev"], IC["chev"], title_plain, s["num"], s["title"].replace(" — ", " — <br>"),
       s["lead"], tags, IC[s["icon"]], feats, title_plain, meta, s["detail"], IC["ext"],
       pills, title_plain, s["detail"], IC["ext"])
  return page(
    "%s — Dr. Nazif Mahbub" % title_plain,
    s["card"],
    "services", body)

# ---------------------------------------------------------------- CONTACT
def contact():
  body = """
<section class="about-hero">
  <div class="wrap">
    <div class="contact-grid">
      <div class="contact-info" data-reveal>
        <span class="kicker">Contact</span>
        <h2 class="display">Let's start a conversation</h2>
        <p>Have a question about coaching, training, MPH admissions, or your podcast? Send a message and Dr. Nazif will get back to you. Every message goes straight to his inbox.</p>
        <div class="contact-cards">
          <a href="mailto:dr.nazif.mahbub@gmail.com">
            <span class="ci">%s</span>
            <span><b>Email</b><span>dr.nazif.mahbub@gmail.com</span></span>
          </a>
          <a href="https://activeactionlab.com" target="_blank" rel="noopener">
            <span class="ci">%s</span>
            <span><b>Active Action Lab</b><span>activeactionlab.com</span></span>
          </a>
          <div>
            <span class="ci">%s</span>
            <span><b>Based in</b><span>Alberta, Canada</span></span>
          </div>
        </div>
      </div>

      <div class="form-card" data-reveal data-reveal-delay="1">
        <form id="contactForm" action="https://formspree.io/f/YOUR_FORM_ID" method="POST" novalidate>
          <div class="field-row">
            <div class="field">
              <label for="name">Name</label>
              <input id="name" name="name" type="text" autocomplete="name" placeholder="Your full name" required>
            </div>
            <div class="field">
              <label for="email">Email</label>
              <input id="email" name="email" type="email" autocomplete="email" placeholder="you@example.com" required>
            </div>
          </div>
          <div class="field">
            <label for="subject">What's this about?</label>
            <select id="subject" name="subject">
              <option value="">Select a topic…</option>
              <option>Personal Development Coaching</option>
              <option>Job Readiness Program</option>
              <option>Corporate Training Workshops</option>
              <option>MPH Admission Coaching</option>
              <option>Podcast Production (Pod Mechanic)</option>
              <option>Podcast guest enquiry</option>
              <option>Something else</option>
            </select>
          </div>
          <div class="field">
            <label for="message">Message</label>
            <textarea id="message" name="message" rows="5" placeholder="Tell me a little about what you're working on…" required></textarea>
          </div>
          <input type="hidden" name="_subject" value="New enquiry from portfolio site">
          <button type="submit" class="btn btn-primary">Send message %s</button>
          <div class="form-status" id="formStatus" role="status" aria-live="polite"></div>
          <p class="form-note">Your message is sent securely to dr.nazif.mahbub@gmail.com.</p>
        </form>
      </div>
    </div>
  </div>
</section>
""" % (IC["mail"], IC["globe"], IC["pin"], IC["arrow"])
  return page(
    "Contact — Dr. Nazif Mahbub",
    "Get in touch with Dr. Nazif Mahbub. Send a message about coaching, corporate training, MPH admissions, or podcast production — delivered straight to his inbox.",
    "contact", body)

# ---------------------------------------------------------------- write all
def write(name, html):
  with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
    f.write(html)
  print("wrote", name)

write("index.html", home())
write("about.html", about())
write("services.html", services_index())
for s in SERVICES:
  write("service-%s.html" % s["key"], service_detail(s))
write("contact.html", contact())
print("done")
