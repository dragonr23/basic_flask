#import app variable instance in order to run application
#also import necessary flask methods


from app import app
from flask import render_template, url_for, redirect




#create the route for the index page, reader the index.html file


@app.route('/')
@app.route('/index')
def index():
    n = 'Max'
    names = ['Smith', 'Kenny', 'Amanda', 'John']
    return render_template('index.html',name=n, names=names, flag=None)
@app.route('/data/<name>',methods=['GET', 'POST'])
def pageData(name=''):

    sports = {
    'football': 'New England Patriots',
    'baseball': 'Boston Red Sox',
    'hockey': 'Boston Bruins',
    'basketball': 'Boston Celtics',
    'soccer': 'New England Revolution'
    }
    return render_template('data.html', name=name, sports=sports)

@app.route('/go_home')
def go_home():
    return redirect(url_for('pageData',name='Max'))
