from tzlocal import get_localzone 
from dateutil import tz
import json
import ast
import redis

#main function
if __name__ == '__main__':
    #connection to redis database
    r = redis.Redis(host='localhost', port=6379, db=0)
    import datetime
    #insert different tasks
    r.hmset("task_1",{"Request_type":"Config","Property":"cpu","time":datetime.datetime(2017, 9, 02, 11, 40 ,20)})
    print r.hgetall('task_1')
    r.hmset("task_2",{"Request_type":"Control","Property":"cpu","time":datetime.datetime(2017,  9, 02, 11, 40 ,21)})
    print r.hgetall('task_2')
    r.hmset("task_3",{"Request_type":"Control","Property":"cpu","time":datetime.datetime(2017,  9, 02, 11, 40 ,22)})
    print r.hgetall('task_3')
