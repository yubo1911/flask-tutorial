# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    app.logger.debug('DEBUG')
    app.logger.warning('WARNING')
    app.logger.error('ERROR')
    return "Hello, World!"
