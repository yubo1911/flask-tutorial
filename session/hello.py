# -*- coding: utf-8 -*-

from flask import Flask, session, escape, request, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as {}'.format(escape(session['username']))

    return 'You are not logged in'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

app.secret_key = '123456'
