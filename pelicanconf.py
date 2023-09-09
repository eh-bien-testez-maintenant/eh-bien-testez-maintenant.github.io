from __future__ import unicode_literals

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['i18n_subsites']

AUTHOR = 'apallier'
SITENAME = 'Eh Bien Testez Maintenant !'
SITESUBTITLE = "Vous codiez ? J'en suis fort aise.<br/> Eh bien : testez maintenant !"
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

# Feed configuration
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
FEED_RSS = 'rss.xml'
RSS_FEED_SUMMARY_ONLY = False

MENUITEMS = (('Archives', '/archives.html'),
             ('Catégories', '/categories.html'),
             ('Tags', '/tags.html'),)

# Social widget
SOCIAL = (
          ('linkedin', 'https://www.linkedin.com/in/alexispallier/'),
          ('rss', '//eh-bien-testez-maintenant.github.io/rss.xml'),
          ('github', 'https://github.com/apallier')
)

# Pages
DISPLAY_PAGES_ON_MENU = True

DEFAULT_PAGINATION = 5

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

STATIC_PATHS = ['images', 'extra', 'doc']
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#
# Language settings
#
# Enable Jinja2 i18n extension used to parse translations.
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
# Default theme language.
I18N_TEMPLATES_LANG = 'en'
# Your language.
DEFAULT_LANG = 'fr'
LOCALE = 'fr_FR'
OG_LOCALE = 'fr_FR'

#
# Flex theme configuration
#
THEME = 'themes/Flex'
SITELOGO = SITEURL + '/images/logo_400x400.jpg'
SITEDESCRIPTION = "Test logiciel, Software Testing, Qualité, Assurance Qualité, QA, Test automatique, Test automation"
MAIN_MENU = True
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}
CUSTOM_CSS = 'static/custom.css'
THEME_COLOR = 'dark'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True
PYGMENTS_STYLE = 'default'
PYGMENTS_STYLE_DARK = 'native'
