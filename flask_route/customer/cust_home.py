from flask import render_template, Blueprint, request, session, redirect, url_for
from route import customer

@customer.route('/')
def home():
    if 'customer_email' not in session:
        return redirect(url_for('customer.login'))
    return render_template('customer/customer_home.html', email = request.args.get('name'))

@customer.route('/logout')
def logout():
    session.pop('customer_email', None)
    return redirect(url_for('customer.login'))
