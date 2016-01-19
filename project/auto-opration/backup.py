#!/usr/bin/python
#coding: utf-8
# Filename: backup_ver1.py

import os
import time

#today=time.strftime('%Y%m%d')
now=time.strftime('%Y%m%d%H%M%S')

def backupDirs(s_dir,target_dir,bak_title,mark_or=False):
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    for i in s_dir:
        os.chdir(i)
        if mark_or == True:
            tmpnote='Mark for the backup --> "%s": '%i
            notice=raw_input(tmpnote)
            if len(notice)!=0:
                target=target_dir + os.sep + bak_title +'_'+ os.path.split(i)[-1]+'_'+now+'_'+notice.strip().replace(' ','_')+'.tar.gz'
            else:
                target=target_dir + os.sep + bak_title +'_'+ os.path.split(i)[-1]+'_'+now+'.tar.gz'
        else:
            print 'Backup --> "%s"'%i
            target=target_dir+os.sep + bak_title +'_'+ os.path.split(i)[-1]+'_'+now+'.tar.gz'
        tar_command='tar -zcf %s .' %target
        if os.system(tar_command)==0:
            print "Successful backup to",target
        else:
            print "Backup Failed"

if __name__=='__main__':
    source=['/data/www','/root/github']
    t_dir='/data/backup'
    backupDirs(source,t_dir,'KRM')
