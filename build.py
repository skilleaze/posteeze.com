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
<nav><a href="/#features">Features</a><a href="/#how">How it works</a><a href="/#faq">FAQ</a><a href="{APP_URL}/auth/login">Sign in</a><a class="btn" href="{APP_URL}/auth">Start free</a></nav>
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
<div class="mock-ai"><span class="spark" aria-hidden="true">&#10022;</span><div><b>AI draft ready</b><small>3 captions for Wednesday, in your brand voice</small></div><span class="mock-btn">Approve</span></div>
</div>"""

INDEX = head("Posteeze: your socials, on autopilot",
             "Plan, write and schedule posts for every channel from one calendar. Posteeze publishes them on time.") + f"""
<section class="hero"><div class="wrap hero-grid">
<div class="hero-copy">
<div class="pill"><span class="dot" aria-hidden="true"></span>Social media scheduling, with AI built in</div>
<h1>Your socials,<br>on <em>autopilot</em>.</h1>
<p class="lead">Plan a month of posts in one sitting. Posteeze writes them with AI, lines them up on one calendar and publishes them to every channel on time.</p>
<div class="cta"><a class="btn btn-lg" href="{APP_URL}/auth">Start free</a><a class="btn btn-lg ghost" href="#how">See how it works</a></div>
<ul class="trust">
<li>{CHECK}Official login for every network</li>
<li>{CHECK}Approve before anything goes live</li>
<li>{CHECK}One calendar for all your brands</li>
</ul>
</div>
{MOCKUP}
</div></section>

<section class="strip" aria-label="Supported channels"><div class="wrap">
<p class="strip-title">Publish to the networks your customers use</p>
<div class="channels">{''.join(f'<span>{c}</span>' for c in CHANNELS)}<span>and more</span></div>
</div></section>

<section id="why"><div class="wrap split">
<div>
<div class="eyebrow">Why Posteeze</div>
<h2>Posting every day is a job. Hand it to autopilot.</h2>
</div>
<div class="compare">
<div class="col before"><h3>Without Posteeze</h3><ul>
<li>Logging in to five apps to post the same update</li>
<li>Writing captions from scratch, every time</li>
<li>Gaps in your feed whenever things get busy</li>
</ul></div>
<div class="col after"><h3>With Posteeze</h3><ul>
<li>Write once, publish everywhere from one place</li>
<li>AI drafts captions in your brand's voice</li>
<li>Posts go out on schedule, even on your busiest days</li>
</ul></div>
</div>
</div></section>

<section id="features"><div class="wrap">
<div class="eyebrow">What you get</div>
<h2>Everything your social calendar needs, in one place.</h2>
<div class="grid">
<div class="card">{ICON(I_CAL)}<h3>One calendar</h3><p>See every post for every channel by day, week or month, and drag to reschedule.</p></div>
<div class="card">{ICON(I_SPARK)}<h3>AI writing</h3><p>Turn an idea into captions and images that fit each platform, in your brand's voice.</p></div>
<div class="card">{ICON(I_AUTO)}<h3>Autopilot</h3><p>Queue posts ahead and they go out at the right time, with retries if a network hiccups.</p></div>
<div class="card">{ICON(I_CHECK)}<h3>Approvals</h3><p>Invite your team or clients to review drafts before anything is published.</p></div>
<div class="card">{ICON(I_CHART)}<h3>Analytics</h3><p>Track reach and engagement per channel and per post, in one view.</p></div>
<div class="card">{ICON(I_TEAM)}<h3>Workspaces</h3><p>Keep each brand or client separate, with its own channels, members and settings.</p></div>
</div>
</div></section>

<section id="how"><div class="wrap">
<div class="eyebrow">How it works</div>
<h2>Set it up once. Posteeze keeps posting.</h2>
<div class="steps">
<div class="card"><h3>Connect your channels</h3><p>Sign in to each network through its official login. Posteeze never sees your passwords.</p></div>
<div class="card"><h3>Plan and write</h3><p>Draft posts yourself or with AI, add media, and place them on the calendar.</p></div>
<div class="card"><h3>Publish on time</h3><p>Posteeze sends each post at its scheduled time and shows you how it performs.</p></div>
</div>
<div class="cta center"><a class="btn btn-lg" href="{APP_URL}/auth">Start free</a></div>
</div></section>

<section id="who"><div class="wrap">
<div class="eyebrow">Built for</div>
<h2>Whoever runs your socials, Posteeze fits.</h2>
<div class="grid three">
<div class="card"><h3>Business owners</h3><p>Keep every channel active without hiring a full-time social media manager.</p></div>
<div class="card"><h3>Agencies</h3><p>Run every client from one login, each in its own workspace with its own approvals.</p></div>
<div class="card"><h3>Marketing teams</h3><p>Plan campaigns together, review drafts and see what performs, in one place.</p></div>
</div>
</div></section>

<section id="faq"><div class="wrap faq-wrap">
<div><div class="eyebrow">FAQ</div><h2>Questions, answered.</h2></div>
<div class="faq">
<details open><summary>Do I need to share my social media passwords?</summary><p>No. You connect each account through the network's own official login, and you can disconnect it any time.</p></details>
<details><summary>Which networks can I post to?</summary><p>Instagram, Facebook, LinkedIn, X, TikTok, YouTube, Threads, Pinterest, Google Business Profile, Reddit, Bluesky, Mastodon, Telegram, Discord and more.</p></details>
<details><summary>Can the AI write in my brand's voice?</summary><p>Yes. Give it an idea and it drafts captions for each platform. You edit or approve before anything is scheduled.</p></details>
<details><summary>Can my team or clients approve posts first?</summary><p>Yes. Invite them to a workspace and drafts wait for review before they are published.</p></details>
<details><summary>Can I manage more than one brand?</summary><p>Yes. Each brand or client gets its own workspace, channels and members.</p></details>
</div>
</div></section>

<section class="final"><div class="wrap final-box">
<h2>Ready to put your socials on autopilot?</h2>
<p>Connect your first channel and schedule this week's posts today.</p>
<div class="cta"><a class="btn btn-lg" href="{APP_URL}/auth">Start free</a><a class="btn btn-lg ghost" href="mailto:{CONTACT}">Talk to us</a></div>
</div></section>

<div class="sticky-cta" aria-hidden="false"><a class="btn" href="{APP_URL}/auth">Start free</a></div>
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
