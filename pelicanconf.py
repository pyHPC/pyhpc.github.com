#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Andy R. Terrel'
SITENAME = u'PyHPC'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [('Home', '/'),
             ('Tutorial', '/tutorial'),
             ('Workshop', '/workshop'),
             ('BoF', '/bof'),
             ('News', '/archives.html')]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


# STATIC_OUT_DIR requires pelican 3.3
STATIC_OUT_DIR = ''
STATIC_PATHS = ['CNAME', 'static']

# Theme
THEME_DIR = os.path.join(os.getcwd(), "theme")
THEME_NAME = "tuxlite_zf"
THEME = os.path.join(THEME_DIR, THEME_NAME)
RECENT_ARTICLES_COUNT = 3

# Blogroll
#LINKS =  (('PyHPC2013 Workshop', 'http://www.dlr.de/sc/en/desktopdefault.aspx/tabid-8685/14943_read-37157/'),)

# Social widget
#SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
