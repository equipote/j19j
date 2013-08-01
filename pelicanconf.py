#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

AUTHOR = u'Equipo Te'
SITENAME = u'Jornadas Estatales DRY 2013'
SITESUBTITLE = u'Subtitulo de la página'
#SITEURL = 'http://jornadas-2013.democraciarealya.es'
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'es'
GITHUB_URL = 'http://github.com/equipote/j19j/'

#PIWIK_URL = u''
#PIWIK_SITE_ID = u''

# Feed generation is usually not desired when developing
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
    ('You can add links in your config file', '#'),
    ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Directorios estáticos:
STATIC_PATHS = ['images']

# Ficheros a copiar (robots.txt, favicon.ico y/u otros)
FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)

LOCALE = ('es_ES.UTF-8')

DEFAULT_DATE = (2013, 7, 19, 14, 1, 1)
DATE_FORMATS = {'es': ('es_ES.UTF-8','%a, %d %b %Y'),}

#THEME = "../temas/mnmlst"

