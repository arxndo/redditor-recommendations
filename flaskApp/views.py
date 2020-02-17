import json
import sys
sys.path.append('neo4j/classes')
sys.path.append('utils/classes')
from NeoReddit import NeoReddit 
from Configuration import Configuration
from flask import render_template, flash, request, redirect
from flaskApp import app

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['text']
        return search_results(name)

    return render_template('home.html')

@app.route('/home', methods=['GET', 'POST'])
def search_results(name):

    cfg = Configuration.configuration('config.yml')
    nr = NeoReddit(cfg)

    authorRecords = nr.authorToAuthors(name, 5)

    if not authorRecords:
        return render_template('error.html' )

    karma = nr.getKarma(name)
    subList = nr.authorToSubs(name, 5)
    selfSubs = []
    for record in subList:
        string = '%s %d%%' % (record[0], round(100*record[1]/karma))
        selfSubs.append(string) 
    

    authors = []
    subInfo = []
    for record in authorRecords:
        authorName = record[0]
        authorKarma = nr.getKarma(authorName)
        string = ''
        authorSubs = nr.authorToSubs(authorName, 3)
        for subRecord in authorSubs:
            string += '%s %d%%, ' % (subRecord[0], round(100*subRecord[1]/authorKarma))
        authors.append(authorName)
        subInfo.append(string[:-2])

    return render_template('results.html',  name = name, \
                                            len=len(authors), \
                                            subs = selfSubs, \
                                            authors = authors, \
                                            otherSubs = subInfo)
