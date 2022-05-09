from distutils.log import debug
from flask import Flask, render_template


app=Flask(__name__)
app.config['SECRET_KEY']='THISISFirst'
# app.config['']
from code_flask import routes


