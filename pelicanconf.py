#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

AUTHOR = u'pobrecito hablador'
SITENAME = u'Jornadas Estatales DRY'
SITESUBTITLE = u'2013'
SITESUBTITLES = ('Left Side', 'Right Side') #Solo en algunos temas puntuales
SITEURL = 'http://jornadas2013.democraciarealya.es'
TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = u'es'
HTML_LANG = 'es'

#DEFAULT_CATEGORY = u'Otras cosas'

TWITTER_USERNAME = '@democraciareal'

REVERSE_ARCHIVE_ORDER = True

TAG_CLOUD_STEPS = 8

MARKUP = (
    (u'rst'),
    (u'md'),
    (u'html'),
)

DISQUS_SITENAME = 'jornadas2013'

GITHUB_URL = 'http://github.com/equipote/j19j/'

#PIWIK_SSL_URL = u''
#PIWIK_URL = u''
#PIWIK_SITE_ID = u''

# Feed generation is usually not desired when developing
FEED_RSS = 'feeds/all.rss.xml'
TAG_FEED_RSS = 'feeds/%s.rss.xml'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('facebook', '#'),
    ('twitter', '#'),
    ('Gitorious', '#'),
    ('Github', '#'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Directorios estáticos:
STATIC_PATHS = ['images', 'sounds', 'grabaciones']

# Ficheros a copiar (robots.txt, favicon.ico y/u otros)
FILES_TO_COPY = (
    ('extra/robots.txt', 'robots.txt'),
    ('extra/favicon.ico', 'favicon.ico'),
)

LOCALE = ('es_ES.UTF-8')

DEFAULT_DATE = (2013, 7, 19, 14, 1, 1)

DATE_FORMATS = {'es': ('es_ES.UTF-8','%d/%m/%Y'),}

FOOTER_TEXT = 'Replace pelican credit'

#THEME = "fresh"
THEME = "skin/"

GOOGLE_CUSTOM_SEARCH = '004640732731469104663:ay2rocw8so8'

PLUGIN_PATH = 'plugins'

PLUGINS = ['assets', 'sitemap', 'gravatar', 'html_rst_directive']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

DELETE_OUTPUT_DIRECTORY = True

#PAGE_DIR = ('pages')

#OUTPUT_PATH = ('/tmp/')

#ARTICLE_EXCLUDES = (('pages',))

#ARTICLE_DIR = ('articles')

#PDF_GENERATOR = False

#YEAR_ARCHIVE_SAVE_AS = True
#MONTH_ARCHIVE_SAVE_AS = True
#DAY_ARCHIVE_SAVE_AS = True

MENUITEMS = (
    ('Inicio', '/'),
)

# global metadata to all the contents
#DEFAULT_METADATA = (('yeah', 'it is'),)

