#!/usr/bin/python


tup = (1,2,3,4,5,6,7,8,9)
li_0 = list(tup) 

for a in list(tup):
    li1 = list(tup)
    li1.remove(a)
    for b in list(tuple(li1)):
        li2 = list(tuple(li1))
        li2.remove(b)
        for c in list(tuple(li2)):
            li3 = list(tuple(li2))
            li3.remove(c)
            for d in list(tuple(li3)):
                li4 = list(tuple(li3))
                li4.remove(d)
                for e in list(tuple(li4)):
                    li5 = list(tuple(li4))
                    li5.remove(e)
                    for f in list(tuple(li5)):
                        li6 = list(tuple(li5))
                        li6.remove(f)
                        for g in list(tuple(li6)):
                            li7 = list(tuple(li6))
                            li7.remove(g)
                            for h in list(tuple(li7)):
                                li8 = list(tuple(li7))
                                li8.remove(h)
                                i = li8[0]
                                if (100*a+10*b+c)*(10*d+e)==(1000*f+100*g+10*h+i):
                                    print ' %s * %s = %s'%(100*a+10*b+c,10*d+e,1000*f+100*g+10*h+i)
