#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "PyHPC Committee"
SITENAME = "PyHPC"
SITEURL = ""
SITELOGO = ("static/images/pyhpc_logo.png", SITENAME, "/")
SITEOGIMAGE = "static/images/pyhpc_logo_og.png"
SITESUMMARY = "PyHPC 2020 - 9th Workshop on Python for High-Performance and Scientific Computing will be happening at Supercomputing 20 on November 13 2020."

# Use the PyHPC theme
THEME = "./theme/pyhpc"

# Workshop Info
WORKSHOP_SHORT_NAME = "PyHPC 2020"
WORKSHOP_FULL_NAME = (
    "9th Workshop on Python for High-Performance and Scientific Computing"
)
WORKSHOP_DATE = "November 13, 2020"
WORKSHOP_LOCATION = "Virtually - Everywhere!"
WORKSHOP_CALL_TO_ACTIONS = [
    ("Call for Submissions", "/submissions"),
    ("Program", "/program"),
]

WORKSHOP_CONF_LOGO = (
    "static/images/sc20_color_black_hor@4x.png",
    "SC20",
    "https://sc20.supercomputing.org",
)
WORKSHOP_CONF_TEXT = "Held in conjunction with SC20: The International Conference for High Performance Computing, Networking, Storage and Analysis"

WORKSHOP_PUB_LOGO = (
    "static/images/tchpc_logo.png",
    "IEEE TCHPC",
    "https://tc.computer.org/tchpc/",
)
WORKSHOP_PUB_TEXT = "In cooperation with"

WORKSHOP_INCLUSIVITY = 'PyHPC is committed to <a href="/inclusivity_statement">inclusivity and accessibility</a>.'

# Front page alert
WORKSHOP_ALERT = (
    "Attention",
"""<div class="space-y-4">
<p>Due to the unprecendented circumstances this year, SC20 will be held virtually.<br/>Please be aware of the following:</p>
<div>
<h3 class="font-bold">Paper submissions</h3>
<ul class="pl-6 list-disc">
   <li>Paper authors must pre-record and submit their presentations by <span class="font-bold">Thursday 8 October</span>.</li>
   <li>Presenters are expected to be available for the duration of their paper session. Question and answers will take place at the end of the session for all presentations given in the session.</li>
</ul>
</div>
<div>
<h3 class="font-bold">Lightning talk submissions</h3>
<ul class="pl-6 list-disc">
   <li>Lightning talks will be presented live and will also be recorded live (no pre-recording needed).</li>
   <li>Lightning talk presentation slides must be submitted by <span class="font-bold">Thursday 8 October</span>.</li>
</ul>
</div>
<p>
The SC20 Virtual team has provided guidance on how to prepare presentation submissions. <a class="font-bold hover:underline" href="https://drive.google.com/file/d/1LjW8Ij6bcOyFaeqna7GA5xEfuSp7ejUo/view?usp=sharing">For a preview of this guidance, please see here.</a></p>
</div>"""
)

# Dates
## Format (Event, Date, completed|in-progress)
WORKSHOP_KEY_DATES = [
    ("Submissions Open", "Monday 1 June", "completed"),
    ("Paper Submissions Due", "Friday 11 September", "completed"),
    ("Paper Author Notifications", "Monday 28 September", "completed"),
    ("Lightning Talk Submissions Due", "Thursday 1 October", "completed"),
    ("Lightning Talk Author Notifications", "Monday 5 October", "completed"),
    ("Paper Camera Ready", "Thursday 8 October", "completed"),
    ("Paper Presentation Recordings", "Thursday 8 October", "completed"),
    ("Lightning Talk Presentation Slides", "Thursday 8 October", "completed"),
    ("Workshop Date", "Friday 13 November", "in-progress"),
]

# Social Media
TWITTER_USERNAME = "PythonHPC"

# Navbar items
DISPLAY_PAGES_ON_MENU = False
PAGE_PATHS = ["pages"]
## Format (Title, Link, External?)
MENUITEMS = [
    ("Call for Submissions", "/submissions", False),
    ("Program", "/program", False),
    ("Updates", "/updates", False),
    ("Registration", "https://sc20.supercomputing.org/attend/register", True),
    ("@PythonHPC", "https://twitter.com/PythonHPC", True),
]

# Pelican Settings
PATH = "content"
TIMEZONE = "US/Central"
DEFAULT_LANG = "en"

ARTICLE_URL = "{date:%Y}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{slug}/index.html"
ARCHIVES_SAVE_AS = 'updates/index.html'
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"
CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

PLUGIN_PATH = "./pelican-plugins"
PLUGINS = ["jinja2content"]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ["CNAME", "static", "robots.txt"]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
