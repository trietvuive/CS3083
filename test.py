from flask import Flask
from flask import render_template

app = Flask("Triet")

@app.route("/")
def hello_world():
    return "<p> Hello, World! </p>"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    return render_template('hello.html', name = name)

@app.route('/login/')
def login():
    return render_template('login.html')
