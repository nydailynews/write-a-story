#!/usr/bin/env python
from flask import g, render_template, url_for, redirect, abort, request
from datetime import datetime, date, timedelta
from collections import OrderedDict
import inspect
import os
import json
import string
from application import app
import filters
from werkzeug.contrib.atom import AtomFeed

datetimeformat = '%Y-%m-%d %H:%M:%S'

def build_url(app, request):
    """ Return a URL for the current view.
        """
    return '%s%s' % (app.url_root, request.path[1:])

# =========================================================
# HOMEPAGE VIEW
# =========================================================

@app.route('/')
def index():
    app.page['title'] = ''
    app.page['description'] = ''
    app.page['url'] = build_url(app, request)
    metadata_all = json.load(filters.json_check('application/chapters.json'))
    metadata = metadata_all['index']

    response = {
        'app': app,
        'metadata': metadata,
    }
    response['prologue'] = render_template('chapters/prologue.html', response=response)
    return render_template('index.html', response=response)

# =========================================================
# NON-HOMEPAGE VIEWS
# =========================================================

@app.route('/about/table-of-contents/')
def toc():
    metadata_all = json.load(filters.json_check('application/chapters.json'))

    app.page['title'] = metadata_all['table-of-contents']['title']
    app.page['description'] = metadata_all['table-of-contents']['description']
    app.page['url'] = build_url(app, request)

    response = {
        'app': app,
        'metadata_all': metadata_all,
        'metadata': metadata_all['table-of-contents'],
    }
    return render_template('table-of-contents.html', response=response)

@app.route('/about/credits/')
def credits():
    metadata_all = json.load(filters.json_check('application/chapters.json'))

    app.page['title'] = metadata_all['credits']['title']
    app.page['description'] = metadata_all['credits']['description']
    app.page['url'] = build_url(app, request)

    response = {
        'app': app,
        'metadata_all': metadata_all,
        'metadata': metadata_all['credits'],
    }
    return render_template('credits.html', response=response)

@app.route('/about/')
def about_index():
    return redirect(url_for('index'))

@app.route('/chapter/')
def chapter_index():
    return redirect(url_for('index'))

@app.route('/chapter/<chapter>/')
def chapter_detail(chapter):
    metadata_all = json.load(filters.json_check('application/chapters.json'))
    metadata = metadata_all[chapter]

    app.page['title'] = ''
    app.page['description'] = ''
    app.page['url'] = build_url(app, request)

    try:
        chapter_display = int(chapter)
    except:
        chapter_display = chapter
    response = {
        'app': app,
        'metadata': metadata,
        'chapter': chapter_display
    }
    response['markup'] = render_template('chapters/%s.html' % chapter, response=response)
    return render_template('chapter_detail.html', response=response)
