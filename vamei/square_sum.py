#!/usr/bin/python
#Filename: square_sum.py

def square_sum(a):
	b=a+1
	c = a**2 + b**2
	return c

for i in range(100):
	j=i+2
	if j**2 == square_sum(i):
		print '%d^2 + %d^2 = %d^2'%(i,i+1,j)
