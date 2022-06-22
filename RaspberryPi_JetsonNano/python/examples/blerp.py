#!/usr/bin/python
# -*- coding:utf-8 -*-
from bottle import route, run, template
import test

@route('/change/<name>')
def index(name):
    return test.picdisplay(name)
  
run(host='0.0.0.0', port=8080)
