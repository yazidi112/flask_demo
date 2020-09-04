# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 10:05:52 2020

@author: imran
"""

from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

if __name__ == '__main__':
    app.run()