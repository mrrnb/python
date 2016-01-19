#!/usr/bin/env python
# coding: utf-8
# Author: Ezreal
# Date: 2016.01.14
# Version: 1.0

import os

keyword='mysqld'
tmpcmd1 = """ ps -fC %s | sed -n '/%s/p'| awk -F' ' '{print $8" --help"}' """%(keyword,keyword)
cmd1 = os.popen(tmpcmd1,'r').read()
tmpcmd2 = """ ps -fC %s | sed -n '/%s/p'| awk '{print $2}' """%(keyword,keyword)
cmd2 = os.popen(tmpcmd2,'r').read()
if cmd2.strip() == '':
    print '%s is no running !'%keyword 
else:
    print 'Now kill Pid:%s'%cmd2,
    os.popen("kill %s"%cmd2,'r').read()
