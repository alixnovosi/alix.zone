#!/usr/bin/env python3

import os
import sys
sys.path.append(os.curdir)

from artdata import *
from projectdata import *
from links import *
from sitedata import *

AUTHOR = "alix"
DEFAULT_LANG = "en"

PATH = "content/"

SITENAME = "alixlog"
SLUGIFY_SOURCE = "title"

THEME = "theme"
TIMEZONE = "America/Los_Angeles"

# feed generation settings
# no feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# author_images plugin
AUTHOR_IMAGES = "images/author_images"

# pages in main menu - done manually instead of letting Pelican help,
# because I have specific ideas about what's linked and what's "secret".
DISPLAY_PAGES_ON_MENU = False

DIRECT_TEMPLATES = ["blog_index", "category", "author", "tag", "archives"]
DEFAULT_PAGINATION = 10
PAGINATED_TEMPLATES = {
    "blog_index": DEFAULT_PAGINATION,
    "category": DEFAULT_PAGINATION,
    "author": DEFAULT_PAGINATION,
    "tag": DEFAULT_PAGINATION,
    "archives": 0,
}
BLOG_INDEX_SAVE_AS = "blog/index.html"

STATIC_PATHS = [
    "gallery",
    "media",
    "extra",  # favicon and robots.txt here.
    "dist",  # javascript
]

EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/humans.txt": {"path": "humans.txt"},
    "extra/keybase.txt": {"path": "keybase.txt"},

    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/android-chrome-192x192.png": {"path": "android-chrome-192x192.png"},
    "extra/android-chrome-512x512.png": {"path": "android-chrome-512x512.png"},
    "extra/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
    "extra/favicon-16x16.png": {"path": "favicon-16x16.png"},
    "extra/favicon-32x32.png": {"path": "favicon-32x32.png"},
    "extra/site.webmanifest": {"path": "site.webmanifest"},
}

TEMPLATE_PAGES = {
    "../theme/templates/home.html": "index.html",
}

# file location settings
ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"
PAGE_URL = "{identifier}.html"
PAGE_SAVE_AS = "{identifier}.html"

PLUGIN_PATHS = [
    "pelican-plugins",
]

PLUGINS = [
    "author_images",
    "touch",
]

DELETE_OUTPUT_DIRECTORY = True

READERS = dict(html=None)
RELATIVE_URLS = False
