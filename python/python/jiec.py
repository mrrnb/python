#!/usr/bin/env python
#coding: utf-8

#一万以内质数阶乘和的后2位 是多少?


def ss(n,s):
	for k in s:
		if k * k > n:
			break
        	if n % k == 0:
			return None
    	return n


def jc(n):
	if n > 0:
		s = jc(n-1)*n
	elif n == 0:
		return 1
	else:
		print 'INPUT ERROR !!!'
	return s

print jc(3)

s = []
for i in range(2,100):
	res = ss(i,s)
	if res:
		s.append(res)
print s
