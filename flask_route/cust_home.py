from flask import render_template, Blueprint, request

cust_home = Blueprint('cust_home', __name__)
@cust_home.route('/home')
def home():
    return render_template('hello.html', name = request.args.get('name'))
