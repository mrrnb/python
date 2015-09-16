#!/usr/bin/python

for o in range(200//6+1):
    for p in range(200//4+1):
        for q in range(200+1):
            if o*6+p*4+q==200:
                print o,p,q


