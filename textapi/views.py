"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from textapi import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/textme', methods = ['GET', 'POST'])
def textme():
    body = request.stream.readlines()
    print(type(body))
    body = str(body[0])
    line = body.split(';')
    data = {}
    data['Name'] = line[0]
    data['ID'] = line[1]
    data['Location'] = line[2]
    return data


