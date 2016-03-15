#!/usr/bin/python
#Filename:leapyear.py

import sys

try:
    i = int(raw_input('Input a year : '))
except:
    print 'Input Error !'
    sys.exit()

if i%4==0:
    if i%100==0 and i%400!=0 or i%3200==0:
        print i,'not leapyear !'
    else:
        print i,'is a leapyear !'
else:
    print i, 'not leapyear !'
