from flask import Flask, render_template, redirect, url_for, request

app = Flask("Triet")

@app.route("/")
def hello_world():
    return "<p> Hello, World! </p>"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    return render_template('hello.html', name = name)

@app.route('/login/', methods = ['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials...'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error = error)

