#!/usr/bin/python

a = 100

def fun():
    if False:
        print "good"
    print a
    return 1
    
if fun():
    print "ok"
