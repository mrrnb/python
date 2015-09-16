#!/usr/bin/python
# Filename: backup_ver1.py

import os
import time

today=time.strftime('%Y%m%d')
now=time.strftime('%H%M%S')

source=['/home/ezreal/python','/home/ezreal/Desktop/ares']
target_dir='/home/ezreal/backup/'+today
target=target_dir+os.sep+now+'.zip'

mkdir_command='mkdir %s'%target_dir
zip_command='zip -qr %s %s' %(target,' '.join(source))

if not os.path.exists(target_dir):
    os.system(mkdir_command)
    print 'Successful created directory',target_dir

if os.system(zip_command)==0:
    print "Successful backup to",target
else:
    print "Backup Failed"
