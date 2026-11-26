#!/usr/bin/env python3
"""Builds the static posteeze.com pages into ./public. Edit the content here, then run it."""
import pathlib, shutil

APP_URL = "https://app.posteeze.com"
SITE_URL = "https://posteeze.com"
CONTACT = "support@posteeze.com"
COMPANY = "[Company legal name]"          # fill in before submitting app reviews
ADDRESS = "[Registered address], Dubai, United Arab Emirates"
UPDATED = "26 November 2026"

OUT = pathlib.Path(__file__).parent / "public"


def head(title, desc, path=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE_URL}/{path}">
<link rel="icon" href="/assets/favicon.ico" sizes="any">
<link rel="icon" type="image/svg+xml" href="/assets/icon.svg">
<link rel="apple-touch-icon" href="/assets/icon-180.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#121417">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Posteeze">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE_URL}/{path}">
<meta property="og:image" content="{SITE_URL}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Posteeze: your socials, on autopilot">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE_URL}/assets/og-image.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Figtree:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header><div class="wrap nav">
<a href="/" aria-label="Posteeze home"><img src="/assets/logo-text-dark.svg" alt="Posteeze" width="170" height="30"></a>
<nav><a href="/#how">How it works</a><a href="/#features">Features</a><a href="/#pricing">Pricing</a><a href="{APP_URL}/auth/login">Sign in</a><a class="btn" href="{APP_URL}/auth">Get started</a></nav>
</div></header>
<main>
"""


FOOT = f"""</main>
<footer><div class="wrap row">
<div>&copy; 2026 Posteeze. All rights reserved.</div>
<nav><a href="/privacy">Privacy</a><a href="/terms">Terms</a><a href="/data-deletion">Data deletion</a><a href="mailto:{CONTACT}">{CONTACT}</a></nav>
</div></footer>
</body>
</html>
"""

ICON = lambda d: f'<div class="ico"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#C6F432" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg></div>'
I_CAL = '<rect x="3" y="4" width="18" height="18" rx="3"/><path d="M16 2v4M8 2v4M3 10h18"/>'
I_SPARK = '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 17l.7 2 2 .7-2 .7-.7 2-.7-2-2-.7 2-.7z"/>'
I_AUTO = '<path d="M21 12a9 9 0 1 1-3-6.7"/><path d="M21 4v5h-5"/>'
I_CHECK = '<path d="M20 6L9 17l-5-5"/>'
I_CHART = '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/>'
I_TEAM = '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17" cy="9" r="2.5"/><path d="M15.5 14.2A5 5 0 0 1 21.5 19"/>'

ORBIT = """<svg class="orbit" viewBox="0 0 64 64" role="img" aria-label="Posteeze orbit mark">
<path d="M46 18 A20 20 0 1 0 52 32" fill="none" stroke="#C6F432" stroke-width="5" stroke-linecap="round"/>
<circle cx="50" cy="20" r="4" fill="#C6F432"/><circle cx="32" cy="32" r="4" fill="#C6F432"/></svg>"""

CHANNELS = ["Instagram", "Facebook", "LinkedIn", "X", "TikTok", "YouTube", "Threads", "Pinterest",
            "Google Business Profile", "Reddit", "Bluesky", "Mastodon", "Telegram", "Discord"]

CHECK = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#C6F432" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6L9 17l-5-5"/></svg>'

MOCKUP = """<div class="mock" role="img" aria-label="Posteeze calendar showing scheduled posts across Instagram, LinkedIn and TikTok">
<div class="mock-bar"><span></span><span></span><span></span><div class="mock-title">Week of 1 December</div></div>
<div class="mock-days">
<div class="day"><b>Mon</b><div class="post ig"><i>IG</i>New collection drop</div><div class="post li"><i>in</i>Hiring: designer</div></div>
<div class="day"><b>Tue</b><div class="post tt"><i>TT</i>Behind the scenes</div></div>
<div class="day"><b>Wed</b><div class="post li"><i>in</i>Client success story</div><div class="post ig"><i>IG</i>Reel: 3 quick tips</div></div>
<div class="day"><b>Thu</b><div class="post fb"><i>f</i>Weekend offer</div></div>
<div class="day"><b>Fri</b><div class="post ig"><i>IG</i>Team Friday</div><div class="post tt"><i>TT</i>Trend remix</div></div>
</div>
<div class="mock-ai"><span class="spark" aria-hidden="true">&#10022;</span><div><b>Trend spotted: new posts ready</b><small>2 designs and 1 video drafted from today's research</small></div><span class="mock-btn">Approve</span></div>
</div>"""

I_SEARCH = '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>'
I_IMAGE = '<rect x="3" y="3" width="18" height="18" rx="3"/><circle cx="9" cy="9" r="2"/><path d="M21 15l-5-5L5 21"/>'
I_VIDEO = '<rect x="2" y="6" width="14" height="12" rx="2"/><path d="M16 10l6-4v12l-6-4z"/>'
I_PEN = '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/>'
I_CLOCK = '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/>'

PLANS = [
  ("Basic", 49, "For a small business getting consistent.", False,
   ["3 social channels", "30 AI posts a month", "AI-designed images and captions", "Weekly industry research", "Auto-scheduling and posting", "1 brand"]),
  ("Standard", 99, "For brands that want video, too.", False,
   ["6 social channels", "60 AI posts a month", "8 AI short videos a month", "Daily trend and industry research", "Auto-scheduling and posting", "1 brand"]),
  ("Pro", 199, "Your full AI social media team.", True,
   ["10 social channels", "120 AI posts a month", "20 AI videos, including cinematic", "Daily research and trend alerts", "Best-time posting", "Team and client approvals"]),
  ("Ultra", 399, "For agencies and multi-brand businesses.", False,
   ["25 social channels", "300 AI posts a month", "50 AI videos, including cinematic", "Everything in Pro", "3 brands", "Priority support"]),
]

def plan_card(name, price, tag, pop, feats):
    cls = "plan pop" if pop else "plan"
    badge = '<div class="badge">Most popular</div>' if pop else ""
    lis = "".join(f"<li>{CHECK}{f}</li>" for f in feats)
    btn = "btn" if pop else "btn ghost"
    return f'''<div class="{cls}">{badge}<h3>{name}</h3><p class="tag">{tag}</p>
<div class="price"><span class="amt">${price}</span><span class="per">/month</span></div>
<a class="{btn} btn-block" href="{APP_URL}/auth?plan={name.lower()}">Choose {name}</a>
<ul>{lis}</ul></div>'''

INDEX = head("Posteeze: your AI social media manager",
             "Posteeze learns your business, researches your industry, designs posts and videos, and publishes to every channel on autopilot.") + f"""
<section class="hero"><div class="wrap hero-grid">
<div class="hero-copy">
<div class="pill"><span class="dot" aria-hidden="true"></span>Now in early access</div>
<h1>Your AI social media manager, on <em>autopilot</em>.</h1>
<p class="lead">Posteeze learns your business, researches your industry every day, designs your posts and videos, and publishes them to every channel at the best time. You approve, it does the rest.</p>
<div class="cta"><a class="btn btn-lg" href="{APP_URL}/auth">Start your autopilot</a><a class="btn btn-lg ghost" href="#pricing">See pricing</a></div>
<ul class="trust">
<li>{CHECK}Set up in 4 simple steps</li>
<li>{CHECK}Plans from $49 a month</li>
<li>{CHECK}Approve posts on WhatsApp, email or in the app</li>
</ul>
</div>
{MOCKUP}
</div></section>

<section class="strip" aria-label="Supported channels"><div class="wrap">
<p class="strip-title">Posts to every network your customers use</p>
<div class="channels">{''.join(f'<span>{c}</span>' for c in CHANNELS)}<span>and more</span></div>
</div></section>

<section id="save"><div class="wrap save">
<div>
<div class="eyebrow">Replace a whole team</div>
<h2>A full social media team, for a fraction of the cost.</h2>
<p class="sub">In Dubai, a social media manager, a designer and a video editor together typically cost <strong>$4,000 to $8,000 a month</strong>. Posteeze does the research, design, video, writing and posting, from <strong>$49 a month</strong>.</p>
<a class="btn btn-lg" href="#pricing">Compare plans</a>
</div>
<div class="vs">
<div class="vs-col"><div class="vs-h">In-house team</div><ul>
<li><span>Social media manager</span><b>$1,600+</b></li>
<li><span>Graphic designer</span><b>$1,100+</b></li>
<li><span>Video editor</span><b>$1,400+</b></li>
</ul><div class="vs-total"><span>Every month</span><b>$4,000+</b></div></div>
<div class="vs-col win"><div class="vs-h">Posteeze Pro</div><ul>
<li><span>Research and strategy</span><b>Included</b></li>
<li><span>Designs and AI videos</span><b>Included</b></li>
<li><span>Writing and posting</span><b>Included</b></li>
</ul><div class="vs-total"><span>Every month</span><b>$199</b></div></div>
<p class="fine">Team costs are typical UAE monthly salaries for each role (PayScale, Naukrigulf, GulfTalent, 2026), converted to USD.</p>
</div>
</div></section>

<section id="how"><div class="wrap">
<div class="eyebrow">How it works</div>
<h2>Set up in 4 steps. Then it runs itself.</h2>
<ol class="flow">
<li><span class="n">1</span><h3>Pick your channels</h3><p>Choose where you post: Instagram, TikTok, LinkedIn, Facebook, YouTube and more.</p></li>
<li><span class="n">2</span><h3>Connect them</h3><p>Sign in through each network's official login. We never see your passwords.</p></li>
<li><span class="n">3</span><h3>Tell the AI about your business</h3><p>Your products, audience, tone and goals. It becomes your brand brief.</p></li>
<li><span class="n">4</span><h3>Choose your plan and go</h3><p>Pick posts per month and where you approve them: the app, email or WhatsApp. Then it plans, designs and schedules.</p></li>
</ol>
<div class="cta center"><a class="btn btn-lg" href="{APP_URL}/auth">Start your autopilot</a></div>
</div></section>

<section id="features"><div class="wrap">
<div class="eyebrow">Every day, on autopilot</div>
<h2>What your AI social media manager does for you.</h2>
<div class="grid">
<div class="card">{ICON(I_SEARCH)}<h3>Researches your industry</h3><p>Checks what is trending in your market every day and turns it into post ideas for your business.</p></div>
<div class="card">{ICON(I_CAL)}<h3>Plans your calendar</h3><p>Builds a month of posts around your goals, offers and key dates, across every channel.</p></div>
<div class="card">{ICON(I_IMAGE)}<h3>Designs your creatives</h3><p>Creates on-brand images, carousels and graphics in your colours and style.</p></div>
<div class="card">{ICON(I_VIDEO)}<h3>Makes your videos</h3><p>AI videos, cinematic clips and motion graphics for Reels, TikTok and Shorts.</p></div>
<div class="card">{ICON(I_PEN)}<h3>Writes every caption</h3><p>Platform-ready captions and hashtags in your brand's voice, for every post.</p></div>
<div class="card">{ICON(I_CLOCK)}<h3>Posts at the best time</h3><p>Publishes everywhere at once, at the times your audience is most active.</p></div>
<div class="card">{ICON(I_CHART)}<h3>Learns what works</h3><p>Tracks reach and engagement, spots what goes viral and does more of it.</p></div>
<div class="card">{ICON(I_CHECK)}<h3>Approve from anywhere</h3><p>Get each post in the app, by email or on WhatsApp and approve with one tap. Or let it run on full autopilot.</p></div>
<div class="card">{ICON(I_TEAM)}<h3>Runs many brands</h3><p>Each brand gets its own brief, channels, calendar and approvals.</p></div>
</div>
</div></section>

<section id="tools"><div class="wrap split">
<div>
<div class="eyebrow">Powered by the best AI</div>
<h2>Cinematic AI video and studio-quality design, built in.</h2>
</div>
<div>
<p class="sub">Posteeze uses leading AI models for writing, image and video, including Higgsfield and Magnific. AI credits are included in every plan.</p>
<div class="chips"><span>Higgsfield</span><span>Magnific</span><span>OpenAI</span><span>Claude</span></div>
<p class="sub small">Already have accounts? Connect your own Higgsfield, Magnific or OpenAI keys to generate beyond your plan. Prefer working in Claude? Connect Posteeze to Claude and run your social media from a chat.</p>
</div>
</div></section>

<section id="pricing"><div class="wrap">
<div class="eyebrow">Pricing</div>
<h2>Simple plans, in US dollars.</h2>
<p class="sub">Every plan includes AI research, design, writing and auto-posting. Change or cancel any time.</p>
<div class="plans">{''.join(plan_card(*p) for p in PLANS)}</div>
</div></section>

<section id="faq"><div class="wrap faq-wrap">
<div><div class="eyebrow">FAQ</div><h2>Questions, answered.</h2></div>
<div class="faq">
<details open><summary>Does it really post by itself?</summary><p>Yes. Once your plan is set, Posteeze creates and schedules your posts and publishes them on time. You can review each post first, or turn on full autopilot.</p></details>
<details><summary>How do I approve posts?</summary><p>Choose during setup: in the Posteeze app, by email, on WhatsApp, or all three. Each preview comes with Approve and Request changes buttons, so you can sign off from your phone in seconds.</p></details>
<details><summary>How does it know my business?</summary><p>During setup you describe your business, audience, offers and tone. Posteeze turns that into a brand brief and uses it for every idea, design and caption.</p></details>
<details><summary>What kind of videos can it make?</summary><p>Short AI videos, cinematic clips and motion graphics sized for Reels, TikTok and YouTube Shorts. The number per month depends on your plan.</p></details>
<details><summary>Do I need to share my social media passwords?</summary><p>No. You connect each account through the network's own official login, and you can disconnect it any time.</p></details>
<details><summary>Can I use my own Higgsfield, Magnific or OpenAI account?</summary><p>Yes. Your plan includes AI credits, and you can connect your own accounts to create more.</p></details>
<details><summary>What currency do you charge in?</summary><p>All plans are priced and billed in US dollars.</p></details>
</div>
</div></section>

<section class="final"><div class="wrap final-box">
<h2>Put your social media on autopilot today.</h2>
<p>Set up in 4 steps. Your first month of posts is ready the same day.</p>
<div class="cta"><a class="btn btn-lg" href="{APP_URL}/auth">Start your autopilot</a><a class="btn btn-lg ghost" href="mailto:{CONTACT}">Talk to us</a></div>
</div></section>

<div class="sticky-cta" id="sticky-cta"><a class="btn" href="{APP_URL}/auth">Start your autopilot</a></div>
<script>
(function(){{var bar=document.getElementById('sticky-cta');if(!('IntersectionObserver' in window)){{bar.classList.add('show');return;}}
var seen=new Set();var io=new IntersectionObserver(function(es){{es.forEach(function(e){{e.isIntersecting?seen.add(e.target):seen.delete(e.target);}});bar.classList.toggle('show',seen.size===0);}});
document.querySelectorAll('.hero .cta, .final-box .cta, .plans').forEach(function(el){{io.observe(el);}});}})();
</script>
""" + FOOT


def doc(path, title, desc, body):
    return head(f"{title} | Posteeze", desc, path) + f"""<div class="wrap"><article class="doc">
<h1>{title}</h1><p class="date">Last updated {UPDATED}</p>
{body}
</article></div>
""" + FOOT


PRIVACY = doc("privacy", "Privacy Policy", "How Posteeze collects, uses and protects your data.", f"""
<p>This policy explains how {COMPANY} ("Posteeze", "we", "us"), {ADDRESS}, handles personal data when you use the Posteeze website and app (the "Service"). Contact us at <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>

<h2>What we collect</h2>
<ul>
<li><strong>Account data:</strong> your name, email address and password (stored hashed), and the workspace you belong to.</li>
<li><strong>Connected social accounts:</strong> when you connect a channel, the platform gives us an access token and basic profile details (account name, ID, profile picture). We never receive your social media password.</li>
<li><strong>Content you create:</strong> posts, captions, images, videos, comments, schedules and settings.</li>
<li><strong>Analytics from platforms:</strong> metrics the platforms return for your connected accounts and posts, such as followers, reach and engagement.</li>
<li><strong>Technical data:</strong> IP address, browser type and logs needed to run and secure the Service.</li>
</ul>

<h2>How we use it</h2>
<ul>
<li>To publish and schedule the content you ask us to, on the accounts you connect.</li>
<li>To show you analytics for your own accounts and posts.</li>
<li>To provide AI writing and image features when you use them.</li>
<li>To run, secure, support and improve the Service, and to contact you about your account.</li>
</ul>
<p>We use data from connected platforms only to provide these features to you. We do not sell personal data, and we do not use platform data for advertising or to build profiles of you.</p>

<h2>Platform-specific terms</h2>
<ul>
<li><strong>YouTube:</strong> Posteeze uses YouTube API Services. By connecting YouTube you also agree to the <a href="https://www.youtube.com/t/terms">YouTube Terms of Service</a>, and Google's handling of data is covered by the <a href="https://policies.google.com/privacy">Google Privacy Policy</a>. You can revoke our access at any time from your <a href="https://myaccount.google.com/permissions">Google security settings</a>.</li>
<li><strong>Meta (Facebook, Instagram, Threads), LinkedIn, X, TikTok, Pinterest and others:</strong> access is granted through each platform's official login and can be revoked in that platform's settings or by disconnecting the channel in Posteeze.</li>
</ul>

<h2>Who we share it with</h2>
<ul>
<li><strong>Social platforms</strong> you connect, to publish your content and fetch your analytics.</li>
<li><strong>Service providers</strong> that host and run the Service on our behalf, including cloud hosting and, when you use AI features, an AI model provider that processes the prompt you submit.</li>
<li><strong>Authorities</strong> where the law requires it.</li>
</ul>

<h2>How long we keep it</h2>
<p>We keep your data while your account is active. When you disconnect a channel we delete its access token. When you delete your account, we delete your account data, connected-account tokens and content within 30 days, except where the law requires us to keep it longer.</p>

<h2>Your rights</h2>
<p>You can access, correct, export or delete your data, and object to or restrict its processing. Email <a href="mailto:{CONTACT}">{CONTACT}</a> or follow the steps on our <a href="/data-deletion">data deletion page</a>.</p>

<h2>Security</h2>
<p>Data is encrypted in transit, access tokens are stored securely, and access to production systems is limited to staff who need it.</p>

<h2>Children</h2>
<p>The Service is not intended for anyone under 18.</p>

<h2>Changes</h2>
<p>We will post changes to this policy here and update the date above. For significant changes we will notify you by email or in the app.</p>
""")

TERMS = doc("terms", "Terms of Service", "The terms that govern your use of Posteeze.", f"""
<p>These terms are an agreement between you and {COMPANY} ("Posteeze", "we"), {ADDRESS}. By creating an account or using the Service you accept them.</p>

<h2>The Service</h2>
<p>Posteeze lets you plan, create, schedule and publish content to social media accounts you connect, and view analytics for them.</p>

<h2>Your account</h2>
<ul>
<li>You must be at least 18 and give accurate information.</li>
<li>You are responsible for activity under your account and for keeping your login details safe.</li>
<li>You may only connect social accounts you own or are authorised to manage.</li>
</ul>

<h2>Your content</h2>
<p>You keep ownership of everything you create or upload. You give us permission to store, process and publish it only as needed to provide the Service. You are responsible for your content and for following each platform's own rules.</p>

<h2>Acceptable use</h2>
<p>Do not use Posteeze to post unlawful, infringing, deceptive or abusive content, to send spam, to manipulate platform engagement, or to try to break or overload the Service.</p>

<h2>Third-party platforms</h2>
<p>Publishing depends on the platforms' own APIs. If a platform changes or limits its API, some features may change or stop working. Your use of each platform is also governed by its terms, including the <a href="https://www.youtube.com/t/terms">YouTube Terms of Service</a> where you connect YouTube.</p>

<h2>Fees</h2>
<p>Any fees for paid plans are shown before you subscribe. [Add billing and refund terms here if you charge for Posteeze.]</p>

<h2>Availability and changes</h2>
<p>We work to keep the Service available but do not guarantee it will be uninterrupted. We may change features, and we will give notice of material changes to these terms.</p>

<h2>Ending your use</h2>
<p>You can stop using the Service and delete your account at any time. We may suspend accounts that break these terms.</p>

<h2>Liability</h2>
<p>To the extent the law allows, the Service is provided "as is", and we are not liable for indirect or consequential losses, or for posts that fail or are delayed because of a third-party platform.</p>

<h2>Governing law</h2>
<p>These terms are governed by the laws of the United Arab Emirates as applied in the Emirate of Dubai.</p>

<h2>Contact</h2>
<p><a href="mailto:{CONTACT}">{CONTACT}</a></p>
""")

DELETION = doc("data-deletion", "Data Deletion", "How to delete your Posteeze data or disconnect a social account.", f"""
<p>You can remove a single connected account, or delete everything Posteeze holds about you.</p>

<h2>Disconnect one social account</h2>
<ol>
<li>Sign in to Posteeze.</li>
<li>Open the channel's menu (the three dots next to it) and choose <strong>Delete Channel</strong>. If the channel still has scheduled posts, delete those first.</li>
<li>We delete that channel's access token straight away. You can also revoke access from the platform's own settings, for example Facebook: Settings &gt; Apps and Websites.</li>
</ol>

<h2>Delete your account and all data</h2>
<p>Email <a href="mailto:{CONTACT}?subject=Delete%20my%20Posteeze%20data">{CONTACT}</a> from the address on your account with the subject "Delete my Posteeze data". We confirm by email and delete your account, connected-account tokens, posts and media within 30 days.</p>

<h2>Requests from Facebook or Instagram</h2>
<p>If you remove Posteeze from your Facebook or Instagram settings, we delete the data we received through that connection. To check the status of a request, email <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
""")

MANIFEST = """{
  "name": "Posteeze",
  "short_name": "Posteeze",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#121417",
  "theme_color": "#121417",
  "icons": [
    {"src": "/assets/icon-192.png", "sizes": "192x192", "type": "image/png"},
    {"src": "/assets/icon-512.png", "sizes": "512x512", "type": "image/png"},
    {"src": "/assets/icon.svg", "sizes": "any", "type": "image/svg+xml"}
  ]
}
"""

if __name__ == "__main__":
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    root = pathlib.Path(__file__).parent
    for f in (root / "assets").iterdir():
        shutil.copy(f, OUT / "assets" / f.name)
    shutil.copy(root / "style.css", OUT / "style.css")
    shutil.copy(root / "assets" / "favicon.ico", OUT / "favicon.ico")
    (OUT / "index.html").write_text(INDEX)
    for name, html in [("privacy", PRIVACY), ("terms", TERMS), ("data-deletion", DELETION)]:
        (OUT / name).mkdir()
        (OUT / name / "index.html").write_text(html)
    (OUT / "site.webmanifest").write_text(MANIFEST)
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    (OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        + "".join(f"<url><loc>{SITE_URL}/{p}</loc></url>" for p in ["", "privacy", "terms", "data-deletion"]) + "</urlset>\n")
    print("built", sorted(str(p.relative_to(OUT)) for p in OUT.rglob("*.html")))
