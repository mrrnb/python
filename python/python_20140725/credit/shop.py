#!/usr/bin/python

f_name = 'shopping.txt'
f = open(f_name,'w')

shop_list = {   
    1 : ['Car',250000],
    2 : ['Iphone',4999],
    3 : ['Coffee',35],
    4 : ['Mac',9688],
    5 : ['Cloths',438],
    6 : ['Bicyle',1500]
    }

for i,v in shop_list.items():
    f.write('%s\t%s\t%s\n'%(i,v[0],v[1]))
f.close()

f = open(f_name)
shop_list = {}

for line in f.readlines():
    li = line.split()
    shop_list[int(li[0])] = [li[1],int(li[2])]
print shop_list
f.close()

