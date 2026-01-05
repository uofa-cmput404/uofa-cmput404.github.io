#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'University of Alberta'
SITENAME = 'CMPUT 404'
SITESUBTITLE = 'Web Applications and Architecture'
SITEURL = ''

PATH = 'content'
THEME = 'templates/cmput404'
TIMEZONE = 'America/Edmonton'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)
LINKS = ()

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {
            'toc_depth': '3-7',
            'baselevel': '3'
        },
        'markdown.extensions.tables': {},
        'markdown.extensions.md_in_html': {},
    },
    'output_format': 'html5',
}
DATE_FORMATS = {
    'en': '%a, %d %b %Y at %H:%M %Z',
}

STATIC_PATHS=[PATH]

PATH_METADATA = r'(?P<path_no_ext>.*)\..*'
SLUGIFY_SOURCE = "basename"
ARTICLE_URL = ARTICLE_SAVE_AS = PAGE_URL = PAGE_SAVE_AS = '{path_no_ext}.html'
STATIC_URL = STATIC_SAVE_AS = '{path}'

DISPLAY_CATEGORIES_ON_MENU=False
DISPLAY_PAGES_ON_MENU=False

INDEX_SAVE_AS="all.html"

MENUITEMS=[
    ("Outline", "/general/outline.html"),
    ("Canvas&Grades", "/#canvas"),
    ("Schedule", "/#schedule"),
    ("Labs", "/general/labs.html"),
    ("Project", "/general/project.html"),
    ("Assignments", "/general/individual.html"),
    ("Resources", "/general/resources.html"),
    ("Discussion Forum", "/general/help.html#discussion-forum"),
    ("News&Notices", "/#news-notices"),
    ("Zoom", "/#lecture-zoom"),
    ("Slides", "https://uofa-cmput404.github.io/slides-xt/"),
    ("Help", "/general/help.html"),
]

