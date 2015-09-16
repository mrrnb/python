#!/usr/bin/python
x=0
while x != 'q':
    x = raw_input("Please input something, q for quit:")
    if not x:
        break
    if x == 'c':
        continue
    print "one more time..."

else:
    print "Ending......"

