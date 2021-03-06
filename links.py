# link configuration.
import os
import sys
sys.path.append(os.curdir)

from projectdata import *

# static pages
PAGES = [
    ("code", "dev.html"),
    ("skills", "skills.html"),
    ("about", "about.html"),

    ("goty2015", "goty2015.html"),
    ("goty2016", "goty2016.html"),
    ("goty2017", "goty2017.html"),
    ("goty2018", "goty2018.html"),
    ("goty2019", "goty2019.html"),
    ("goty2020", "goty2020.html"),
    ("goty2021", "goty2021.html"),
    ("goty2010s", "goty2010s.html"),

    ("books", "books2018.html"),
    ("books", "books2019.html"),
    ("books", "books2020.html"),
    ("books", "books2021.html"),
]

# social links
SOCIAL = {
    "twitter": {
        "link": "https://twitter.com/alixnovosi",
        "icon_link": "/media/social/twitter.svg",
    },
    "github": {
        "link": GIT_ROOT,
        "icon_link": "/media/social/github.png",
    },
    "itch.io": {
        "link": ITCH_ROOT,
        "icon_link": "/media/social/itchio.svg",
    },
    "twitch": {
        "link": "https://twitch.tv/alixnovosi",
        "icon_link": "/media/social/twitch.svg",
    },
    "youtube": {
        "link": "https://youtube.com/alixnovosi",
        "icon_link": "/media/social/youtube.png",
    },
}

# pages that go into their own little zones.
# with possibly different nav
SUBPAGES = [
    ("blog", "blog/index.html"),
    ("goty", "goty2021.html"),
    ("goty10s", "goty2010s.html"),
    ("books", "books2021.html"),
]

TOPLEVEL_PAGES = [
    ("about", "about.html", "about"),
    ("toys", "toybox.html", "toybox"),
    ("art", "ocgallery.html", "ocgallery"),
    ("code", "dev.html", "dev"),
    ("skills", "skills.html", "skills"),
]
