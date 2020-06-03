#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "PyHPC Committee"
SITENAME = "PyHPC"
SITEURL = ""
SITELOGO = ("static/images/pyhpc_logo.png", SITENAME, "/")

# Use the PyHPC theme
THEME = "./theme/pyhpc"

# Workshop Info
WORKSHOP_SHORT_NAME = "PyHPC 2020"
WORKSHOP_FULL_NAME = (
    "9th Workshop on Python for High-Performance and Scientific Computing"
)
WORKSHOP_DATE = "November 15, 2020"
WORKSHOP_LOCATION = "Atlanta, GA"
WORKSHOP_CALL_TO_ACTIONS = [
    ("Call for Participation", "/cfp"),
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

# Dates
## Format (Event, Date, completed|in-progress)
WORKSHOP_KEY_DATES = [
    ("Submissions Open", "Monday 1 June", "completed"),
    ("Paper Submissions Due", "Friday 4 September", "in-progress"),
    ("Paper Author Notifications", "Monday 28 September", ""),
    ("Lightning Talk Submissions Due", "Thursday 1 October", ""),
    ("Paper Camera Ready", "Thursday 8 October", ""),
    ("Lightning Talk Author Notifications", "Monday 19 October", ""),
    ("Paper Presentation Slides", "Monday 2 November", ""),
    ("Workshop Date", "Sunday 15 November", ""),
]

# Social Media
TWITTER_USERNAME = "PythonHPC"

# Navbar items
DISPLAY_PAGES_ON_MENU = False
PAGE_PATHS = ["pages"]
## Format (Title, Link, External?)
MENUITEMS = [
    ("Call for Participation", "/cfp", False),
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
