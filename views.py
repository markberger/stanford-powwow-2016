from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/booth.html')
def booth():
	return render_template('booth.html')

@app.route('/contesting.html')
def contesting():
    return render_template('contesting.html')

@app.route('/fun-run.html')
def fun_run():
    return render_template('fun-run.html')
