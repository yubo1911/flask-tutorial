# -*- coding: utf-8 -*-

from flask import Flask, redirect, abort, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    abort(401)
    return 'This will never return'


@app.errorhandler(404)
def page_not_found(error):
    return 'PAGE NOT FOUND', 404
