#!/usr/bin/python

j=0
k=100
list1=[1,11,111,200,300,4000,500,22222,1111,100,5,81,2,38,91,66]
print ','.join([str(i) for i in list1])
#print ','.join(len(list1)*'%s')%tuple(list1)
for i in list1:
	if i>j:
		j=i
	if i<k:
		k=i
print "\nThe small one is %d, and the big one is %d\n"%(k,j)
