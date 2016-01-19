#!/usr/bin/python



#  ^^^ * ^^ = ^^^^

print '111 * 11 == 1111'

for o in range(100,1000):
    for p in range(10,100):
        for q in range(1000,10000):
            if o * p == q:
                pass
            #    print o,p,q
            a = o//100
            b = o//10
            c = o%10
            print a,b,c
            break

