import json
import sys
sys.path.append('neo4j/classes')
sys.path.append('utils/classes')
from NeoReddit import NeoReddit 
from Configuration import Configuration
from flask import render_template, flash, request, redirect
from flaskApp import app
from forms import RedditorSearchForm

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    #search = RedditorSearchForm(request.form)
    if request.method == 'POST':
        name = request.form['text']
        return search_results(name)

    return render_template('home.html')


@app.route('/results', methods=['GET', 'POST'])
def search_results(name):

    cfg = Configuration.configuration('config.yml')
    nr = NeoReddit(cfg)

    authors = nr.authorToAuthors(name, 3)

    item1 = nr.authorToSubs(authors[0], 3)
    subName1 = []
    for sub in item1:
        print(sub[0])
        subName1.append(sub[0])

    item2 = nr.authorToSubs(authors[1], 3)
    subName2 = []
    for sub in item2:
        subName2.append(sub[0])

    item3 = nr.authorToSubs(authors[2], 3)
    subName3 = []
    for sub in item3:
        subName3.append(sub[0])

    if not authors:
        return render_template('error.html' )
    else:
        return render_template('results.html', name1=authors[0], \
                                                name2=authors[1], \
                                                name3=authors[2], \
                                                sub11=subName1[0], \
                                                sub12=subName1[1], \
                                                sub13=subName1[2], \
                                                sub21=subName2[0], \
                                                sub22=subName2[1], \
                                                sub23=subName2[2], \
                                                sub31=subName3[0], \
                                                sub32=subName3[1], \
                                                sub33=subName3[2], \
                                                )



@app.route('/subs')
def subs():
    cfg = Configuration.configuration('config.yml')
    nr = NeoReddit(cfg)
    subs = nr.authorToSubs('kn0thing', 10)
    string = ''
    for sub in subs:
        string += '\n%s' % sub[0]
    return string
