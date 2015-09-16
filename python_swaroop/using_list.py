#!/usr/bin/python
# Filename: using_list.py

shoplist=['apple','mango','carrot','banana']
print len(shoplist)

for item in shoplist:
    print item,

shoplist.append('rice')

print '\n',shoplist

shoplist.sort()
print shoplist

print shoplist[0]
olditem=shoplist[0]
print olditem
del shoplist[0]
print shoplist[0]
print shoplist
