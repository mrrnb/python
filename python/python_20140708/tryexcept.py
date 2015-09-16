#!/usr/bin/python

try:
	fsock = open('filename', "rb", 0)
	try:
		fsock.seek(-128,2)
		tagdata=fsock.read(128)
	finally:
		fsock.close()

except IOError:
	pass
