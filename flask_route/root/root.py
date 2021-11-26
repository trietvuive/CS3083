from flask import Blueprint, render_template, request
from route import home
from settings import *

@home.route('/')
def hello_world():
    return render_template('root/root.html')
