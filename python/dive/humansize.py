#!/usr/bin/python 


SUFFIXES = {1000 : ['KB','MB','GB','TB','PB','EB','ZB','YB'],
			1024 : ['KiB','MiB','GiB','TiB','PiB','EiB','ZiB','YiB']}

def approximate_size(size,a_kilobyte_is_1024_bytes=True):

	'''
Convert a file size to human-readable form.

Keyword arguments:
size --- file size in bytes
a_kilobyte_is_1024_bytes -- if True(default), use multiples of 1024
							if False, use multiples of 1000


Ruturns: string
'''

	if size < 0:
		raise ValueError('number must be non-negative')

	multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
	for suffix in SUFFIXES[multiple]:
#		size /= multiple
		if size < multiple:
			return '{0:.1f} {1}'.format(size, suffix)
		size /= multiple

	raise ValueError('number too large')

if __name__=='__main__':
	print (approximate_size(500000000000,False))
	print (approximate_size(500000000000))
