from time import sleep
from datetime import datetime
from datetime import timedelta

import json

i=0
while i<1:
    
    ts_current = datetime.utcnow().replace(microsecond=0)
    print(ts_current)
    
    ts_timer = ts_current + timedelta(minutes=0,seconds=1)
    print(ts_timer)
    
    #print(datetime.utcnow() < ts_timer)
    #ts_final = datetime(ts_now.year, ts_now.month, ts_now.day, ts_now.hour, ts_now.minute, ts_now.second+1)
    #print(ts_final)
    
    while (datetime.utcnow() < ts_timer):
        #print(datetime.utcnow())
        sleep(0.05)
    
    print("Timer went off: ")
    print((ts_timer))
    print((datetime.utcnow()))
    
    i+=1
    
# test json

data = {}
data['default'] = [1,2,54,2,3]
data['rd'] = [2250]
data['tc'] = 17.0
data['timestamp'] = datetime.utcnow().replace(microsecond=0).isoformat()

print(data)

print(json.dumps(data,indent=4))

with open('data.txt','w') as of:
    json.dump(data,of,indent=4)