#!/usr/bin/python
# Filename: 

filename='while.txt'
s=0

f = file(filename,'r')
for line in f.readlines():
	if(len(line)>s):
		s=len(line)
print s

f.close()
