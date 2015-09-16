#!/usr/bin/python
# Filename: stat.py

li=[8.0,8.0,4.0,4.0,4.0,11.0,4.0]
dic={}
for item in li:
    if item in dic.keys():
        dic[item]+=1
    else:
        dic[item]=1
print dic



d = {k:li.count(k) for k in set(li)}
print d
