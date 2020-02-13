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
    search = RedditorSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('home.html', form=search)


@app.route('/results', methods=['GET', 'POST'])
def search_results(search):
    search = RedditorSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    results = []
    search_string = search.data['search']

    if search.data['search'] == '':
        results = 'something'

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        return render_template('results.html', results=results)


@app.route('/subs')
def subs():
    cfg = Configuration.configuration('config.yml')
    nr = NeoReddit(cfg)
    subs = nr.authorToSubs('kn0thing', 10)
    string = ''
    for sub in subs:
        string += '\n%s' % sub[0]
    return string
