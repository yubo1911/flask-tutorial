# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

app.secret_key = 'secret_key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            flash('Invalid credentials', 'error')
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))

    return render_template('login.html', error=error)
