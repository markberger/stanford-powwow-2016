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
