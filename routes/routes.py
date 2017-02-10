# -*- coding: utf-8 -*-

from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Index"


@app.route('/hello')
def hello_world():
    return "Hello, World!"


@app.route('/user/<username>')
def user_profile(username):
    return "user: {}".format(username)


@app.route('/post/<int:post_id>')
def post(post_id):
    return "post: {}".format(post_id)


@app.route('/print_url')
def print_url():
    return "{}<br/>{}<br/>{}<br/>{}".format(
            url_for('index'),
            url_for('hello_world', parma='p'),
            url_for('user_profile', username='yubo'),
            url_for('post', post_id=2, param='q'))
