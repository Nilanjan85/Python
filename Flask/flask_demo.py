# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 20:40:05 2021

@author: User
"""
from flask import Flask

app =  Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1> Hello World! </h1>"

@app.route("/about")
def about():
    return "<h1> About Page </h1>"

    
if __name__ == "__main__":
    app.run(debug=True)

