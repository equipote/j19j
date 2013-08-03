#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

AUTHOR = u'Jornadas J-19 2013'
SITENAME = u'Jornadas Estatales DRY 2013'
SITESUBTITLE = u'Subtitulo de la página'
SITESUBTITLES = ('Left Side', 'Right Side') #Solo en algunos temas puntuales
#SITEURL = 'http://jornadas-2013.democraciarealya.es'
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'es'

HTML_LANG = 'es'
TWITTER_USERNAME = '@democraciareal'

REVERSE_ARCHIVE_ORDER = True
TAG_CLOUD_STEPS = 8

MARKUP = ((u'rst'),)

DISQUS_SITENAME = ''

GITHUB_URL = 'http://github.com/equipote/j19j/'

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
    ('Facebook', '#'),
    ('Twitter', '#'),
    ('Gitorious', '#'),
    ('Github', '#'),
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Directorios estáticos:
STATIC_PATHS = ['images', 'sounds']

# Ficheros a copiar (robots.txt, favicon.ico y/u otros)
FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)

LOCALE = ('es_ES.UTF-8')

DEFAULT_DATE = (2013, 7, 19, 14, 1, 1)
DATE_FORMATS = {'es': ('es_ES.UTF-8','%d/%m/%Y'),}

FOOTER_TEXT = 'Replace pelican credit'

THEME = "fresh"

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

