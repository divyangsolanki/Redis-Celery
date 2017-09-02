''' File : celery worker file 
    Created by : Divyang solanki
'''
#import libraries
from __future__ import absolute_import
from rediscelery.celery import app
import time

#addision task
@app.task
def add(x, y):
    return x + y
#multiplication task
@app.task
def mul(x,y):
    return x*y