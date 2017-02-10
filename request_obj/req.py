# -*- coding: utf-8 -*-

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello, World!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    return '{}<br/>{}'.format(
            request.method,
            request.args
            )
