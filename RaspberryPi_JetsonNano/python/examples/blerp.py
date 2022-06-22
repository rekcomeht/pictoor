#!/usr/bin/python
# -*- coding:utf-8 -*-
from bottle import route, run, template
import test, boot

@route('/change/<name>')
def index(name):
    return test.picdisplay(name)

@route('/boot/')
def index():
    return boot.boot()
  
run(host='0.0.0.0', port=8080)
