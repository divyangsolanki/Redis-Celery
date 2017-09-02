''' File : celery worker file 
    Created by : Divyang solanki
'''
#import libraries
from .tasks import add,mul
import redis
import pandas
import pytz
from tzlocal import get_localzone 
from dateutil import tz
import time

#utc conversion function
def  utc_convert_time(time):
    from datetime import datetime,timedelta
    #get localtime zone
    tz = get_localzone()
    datetime_with_tz = tz.localize(time, is_dst=None)
    #convert time to utc
    datetime_in_utc = datetime_with_tz.astimezone(pytz.utc)
    convert_time = pandas.to_datetime(datetime_in_utc).to_pydatetime()
    return convert_time

#main function
if __name__ == '__main__':
    #connect to redis database
    r = redis.Redis(host='localhost', port=6379, db=0)
    print "Worker process starterd"
    
    while(True):
        
        #get current time
        import datetime
        cur = datetime.datetime.now().replace(microsecond=0)
        cur_time = utc_convert_time(cur)
        
        #iterate through all keys of redis database
        for key in r.scan_iter(match='task_*'):
            #extract time from key-value pair
            redis_t = r.hgetall(key)['time']
            from datetime import datetime,timedelta
            datetime_without_tz = datetime.strptime(redis_t,"%Y-%m-%d %H:%M:%S")
            redis_time = utc_convert_time(datetime_without_tz)
                       
            if str(cur_time) == str(redis_time):
                #if request is control
                if(r.hgetall(key)['Request_type']== 'Control'):
                    result = add.apply_async(args=[500,50],eta=redis_time )
                    print "Control task done"
                    
                #if request is config
                if(r.hgetall(key)['Request_type']== 'Config'):
                    result = mul.apply_async(args=[500,50],eta=redis_time )
                    print "Config task done"
                time.sleep(1)
                
