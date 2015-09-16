#!/usr/bin/python
# Filename: cat2.py

import sys

def readfile(filename):
    f=file(filename)
    while True:
        line=f.readline()
        if len(line)==0:
            break
        print line,
    f.close()

if len(sys.argv)<2:
    print 'No action specified'
    sys.exit()

if sys.argv[1].startswith('--'):
    option=sys.argv[1][2:]
    if option=='version':
        print 'Version1.2'
    elif option=='help':
        print 'This is the help file'
    else:
        print 'Unknown option'
    sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)
