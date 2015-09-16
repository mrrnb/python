#! /usr/bin/python
# Filename: account.py

def denglu(u,p):
	f = file('account.txt','r')
	for line in f.readlines():
		li = line.split()
		print li


denglu('ezreal','osatmnzn')
