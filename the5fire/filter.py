#!/usr/bin/python

self.addFilter(r'\*(.+?)\*', 'emphasis')
self.addFilter(r'(http://[\.a-z0-9A-Z/]+)', 'url')
self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)','mail')
