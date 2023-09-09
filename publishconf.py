# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://eh-bien-testez-maintenant.github.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
DISQUS_SITENAME = 'eh-bien-testez-maintenant'
GOOGLE_GLOBAL_SITE_TAG = "G-EKML3CYE6E"
# Flex theme configuration
SITELOGO = SITEURL + '/images/logo_400x400.jpg'
COPYRIGHT_YEAR = 2023
