#!/usr/bin/python
# Filename: leip.py

li = [1,2,3,4,5,6,7,8,9,0]

for i in li:
	print li[0]
	li.pop(li[0])
	print li
	for j in li:
		li.pop(li[0])
		for k in li:
			li.pop(li[0])
			for l in li:
				li.pop(li[0])
				print i,j,k,l,li
