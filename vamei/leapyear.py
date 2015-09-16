#!/usr/bin/python
#Filename:leapyear.py

for i in range(1800,2201):
	if i%4==0:
		if i%100==0 and i%400!=0 or i%3200==0:
			print i,"no"
		else:
			print i
