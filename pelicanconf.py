#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['i18n_subsites']

AUTHOR = 'apallier'
SITENAME = 'Eh Bien Testez Maintenant !'
SITESUBTITLE = "Vous codiez ? J'en suis fort aise.<br/> Eh bien : testez maintenant !"
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_RSS = 'rss.xml'

MENUITEMS = (('Archives', '/archives.html'),
             ('Catégories', '/categories.html'),
             ('Tags', '/tags.html'),)

# Social widget
SOCIAL = (('github', 'https://github.com/eh-bien-testez-maintenant'),
          ('twitter', 'https://twitter.com/EhBienTestezMnt'),
          ('rss', '//eh-bien-testez-maintenant.github.io/rss.xml'))

# Pages
DISPLAY_PAGES_ON_MENU = True

DEFAULT_PAGINATION = True
DEFAULT_PAGINATION = 10

THEME = 'themes/flex'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'


STATIC_PATHS = ['images', 'extra', 'doc']
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Language settings
# Enable Jinja2 i18n extension used to parse translations.
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
# # Default theme language.
I18N_TEMPLATES_LANG = 'en'
# Your language.
DEFAULT_LANG = 'fr'
LOCALE = 'fr_FR'
OG_LOCALE = 'fr_FR'

# Flex theme configuration
SITELOGO = SITEURL + '/images/logo_400x400.jpg'
SITEDESCRIPTION = "Test logiciel, Software Testing, Qualité, Assurance Qualité, QA"
MAIN_MENU = True

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'