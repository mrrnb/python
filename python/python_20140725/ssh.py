#!/usr/bin/python

import os

username = 'root'
ip = 'localhost'
cmd = 'df'

def runCmd(uname,host,command = ''):
    CMD = 'ssh -p 22222 %s@%s %s'%(uname,host,command)
    print CMD
    os.system(CMD)
    print '\033[32;1mExit from %s, bye !!!\033[0m'%host

runCmd(username,ip)
