#!/usr/bin/env python
import os
import json
from flask import Flask
from flask import Markup
from flask_flatpages import FlatPages
from datetime import date

app = Flask(__name__)
app.debug = True

# This dict is called on every .html document.
# We initialize it here in case all the fields aren't defined by the view method.
page = {
    'title': '',
    'url': '',
    'description': '',
    'author': '"Gersh Kuntzman", "Interactive Fiction"',
    'datestamp': '',
    'keywords': '',
    'keywords_array': '',
    'shareimg': '',
    'shareimgdesc': '',
}

pages = FlatPages(app)

# SITE CONFIG
# Most of these vars are used on the site in some way.
# We store them here and then pass them to the template (you see them as response.app....)
fh = open('application/chapters.json')
metadata_all = json.load(fh)
with app.app_context():
    app.url_root = '/'
    app.page = page
    app.sitename = ''
    app.chapters_all = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','epilogue','acknowledgements', 'prologue']
    app.chapters = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','epilogue','acknowledgements']
    app.metadata = metadata_all

import application.flatpage
import application.thesite
