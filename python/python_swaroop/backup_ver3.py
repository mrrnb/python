#!/usr/bin/python
# Filename: backup_ver1.py

import os
import time

today=time.strftime('%Y%m%d')
now=time.strftime('%H%M%S')

source=['/home/ezreal/python','/home/ezreal/Desktop/ares']
target_dir='/home/ezreal/backup/'+today
notice=raw_input('Enter a comment for the backup --> ')
if len(notice)==0:
    target=target_dir+os.sep+now+'.zip'
else:
    target=target_dir+os.sep+now+'_'+notice.replace(' ','_')+'.zip'

# mkdir_command='mkdir %s'%target_dir
zip_command='zip -qr %s %s' %(target,' '.join(source))

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print 'Successful created directory',target_dir

if os.system(zip_command)==0:
    print "Successful backup to",target
else:
    print "Backup Failed"
