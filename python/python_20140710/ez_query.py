#!/usr/bin/python
# -*- coding:UTF-8 -*-

import sys
if len(sys.argv) <= 1:
    file_name='query.txt'
else:
    file_name=sys.argv[1]
fi = file(file_name)
s_file = fi.readlines()
fi.close()
running = True

#函数cat, 用来打印出整个文件
def cat(f):                   #参数必须为一个列表
    for line in f:
        print line,
    else:
        pass

#函数search, 用来查询关键字, 在文件中
def search(f):
    run = True
    while run:
        key_exist = False
        user_input = raw_input('What do you want to search: ')
        if len(user_input) == 0:
            continue
        for line in f:
            if user_input in line:
                print line
                key_exist = True
            elif user_input == 'exit':
                run = False
                break
        else:
            if not key_exist:
                print 'Can not Search keyword !!!'

#函数add, 用来增加文件中的行
def add(f):
    run = True
    while run:
        user_input = raw_input('What do you want to add :') 
        input_count=0
        if len(user_input) == 0:
            continue
        else:
            input_count+=1
        f.append(user_input)
        print user_input
        fi2 = file(file_name,'a')
        for line in f[-input_count:]:
            fi2.write(str(f.index(line)+1)+'\t'+line+'\n')
        if user_input == 'exit':
            run = False
            break

#函数delete, 用来删除文件中的行

#函数insert, 用来插入行

#函数update, 用来修改行

#主程序

dic = {'c':cat,
        's':search,
        'a':add
        #'d':delete,
        #'i':insert,
        #'u':update
        }

while running:
    u_order = raw_input('Choose a Order in\n\t(cat,search,add,del,insert,update)\n>>> ')
    for order in dic:
        if u_order == order:
            dic[order](s_file) 
        elif u_order == 'quit' or u_order == 'q' or u_order == 'exit':
            exit()






