#!/usr/bin/env python

import os
import time

timeArray=time.localtime(time.time())
nowdate = time.strftime("%Y-%m-%d", timeArray).replace('-0','-')
print nowdate

cmd1 = """cat /app/umo_script/data_log/refer_%s*|awk -F '|' '{a[$28]+=1}END{for(b in a){print b "=" a[b]}}'"""%nowdate
os.system(cmd1)

