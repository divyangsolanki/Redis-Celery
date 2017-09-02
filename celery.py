''' File : celery worker file 
    Created by : Divyang solanki
'''
#import libraries
from __future__ import absolute_import
from celery import Celery

#connection to rabbitmq broker and include task file
app = Celery('rediscelery',
             broker='amqp://test:test@localhost/test_vhost',
             backend='rpc://',
             include=['rediscelery.tasks'])