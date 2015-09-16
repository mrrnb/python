#!/usr/bin/python
# Filename: backup_ver1.py

import os
import time

source=['/home/ezreal/python','/home/ezreal/Desktop/ares']
target_dir='/home/ezreal/backup/'
target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'
zip_command='zip -qr %s %s' %(target,' '.join(source))

if os.system(zip_command)==0:
    print "Successful backup to",target
else:
    print "Backup Failed"
