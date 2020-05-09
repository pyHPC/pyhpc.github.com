#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'PyHPC Committee'
SITENAME = 'PyHPC'
SITEURL = ''

# Use the PyHPC theme
THEME = './theme/pyhpc'

# Workshop Info
WORKSHOP_SHORT_NAME = 'PyHPC 2020'
WORKSHOP_FULL_NAME = '9th Workshop on Python for High-Performance and Scientific Computing'
WORKSHOP_DATE = 'November 15, 2020'
WORKSHOP_LOCATION = 'Atlanta, GA'
WORKSHOP_CALL_TO_ACTION = ('Call for Participation', '#')
# WORKSHOP_HERO_IMAGE = ""
# WORKSHOP_HERO_IMAGE_ALT = ""
WORKSHOP_CONF_LOGO = "static/images/sc20_color_black_hor@4x.png"

# Dates
KEY_DATES = [('Paper Submissions Due', 'Friday 4 September', 'completed'),
             ('Paper Author Notifications', 'Monday 28 September', 'in-progress'),
             ('Lightning Talk Submissions Due', 'Thursday 1 October', ''),
             ('Paper Camera Ready', 'Thursday 8 October', ''),
             ('Lightning Talk Author Notifications', 'Monday 19 October', ''),
             ('Workshop Date', 'Sunday 15 November', '')]

# Social Media
TWITTER_USERNAME = 'pyhpc'

# Navbar items
DISPLAY_PAGES_ON_MENU = False
PAGE_PATHS = ['pages']
MENUITEMS = [('Home', '/'),
            ('News', '/archives')]

# Pelican Settings
PATH = 'content'
TIMEZONE = 'US/Central'
DEFAULT_LANG = 'en'

ARTICLE_URL = '{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

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
