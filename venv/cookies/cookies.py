# -*- coding: utf-8 -*-

from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    resp = make_response("Hello, World!")
    resp.set_cookie('username', 'yubo')
    return resp


@app.route('/cookie')
def print_cookie():
    username = request.cookies.get('username')
    return username
