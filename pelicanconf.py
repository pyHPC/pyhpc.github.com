#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'PyHPC Committee'
SITENAME = 'PyHPC'
SITEURL = ''

# Use the PyHPC theme
THEME = './theme/pyhpc'

# Workshop Info
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
    ("Workshop Date", "Sunday 15 November", ""),
]

# Social Media
TWITTER_USERNAME = 'PythonHPC'

# Navbar items
DISPLAY_PAGES_ON_MENU = False
## Format (Title, Link, External?)
MENUITEMS = [
    ("Call for Participation", "/cfp", False),
    ("Program", "/program", False),
    ("Updates", "/updates", False),
    ("Registration", "https://sc20.supercomputing.org/attend/register", True),
    ("@PythonHPC", "https://twitter.com/PythonHPC", True),
]

# Pelican Settings
PATH = 'content'
TIMEZONE = 'US/Central'
DEFAULT_LANG = 'en'

PLUGIN_PATH = "./pelican-plugins"
PLUGINS = ["shortcodes", "jinja2content"]
SHORTCODES = {
    # image
    "image": "<img class={{class}} src=static/images/{{src}} alt={{alt}}></img>",
    "important_link": "<a class='block mx-auto p-4 border border-gray-600 rounded-md text-xl text-center' href='{{url}}{{extra}}'>{{text}}</a>",
    "important_email": "<a class='block mx-auto p-4 border border-gray-600 rounded-md text-xl text-center' href='mailto:{{email}}?subject={{subject}}'>{{text}}</a>",
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['CNAME', 'static', 'robots.txt']

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
