#!/usr/bin/env python
# coding: utf-8
# Author: Ezreal
# Date: 20151217
# Version: 1.0

import os
import sys

#带颜色输出
def color_print(msg, color='blue'):
    """Print colorful string."""
    color_msg = {'blue': '\033[1;36m%s\033[0m',
                 'green': '\033[1;32m%s\033[0m',
                 'red': '\033[1;31m%s\033[0m'}
    print color_msg.get(color, 'blue')%msg


#获取文件列表
filelist = []
with file('/etc/crontab','r') as f:
    lines = f.readlines()
    for i in lines:
        for j in i.split():
            if 'app/run' in j:
                if os.path.exists(j):
                    filelist.append(j)
                else:
                    color_print(j + ' is not exists!')

#定义修改文件函数
def modify_file(filename,sstr,rstr):
    with open(filename,'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if sstr in lines[i]:
                lines[i] = lines[i].replace(sstr,rstr)
    with open(filename,'w') as f:
        f.writelines(lines)

#打印文件列表中包含app/config的行及修改
def show(modify=False):
    for i in filelist:
        with file(i,'r') as f:
            lines = f.readlines()
            for j in lines:
                if 'Main.config.inc' in j:
                    if modify:
                        tmpli = i.split('run')
                        tmpstr = j.split()[1]
                        tmpstr1 = "'" + tmpli[0] + "config/Main.config.inc';"
                        modify_file(i,tmpstr,tmpstr1)
                    else:
                        print('%-56s%s')%(i,j.strip())

def main():
    if len(sys.argv) >= 2 and sys.argv[1] == 'modify':
        show(True)
        show()
    else:
        show()
        color_print("### 要执行修改操作，请加modify参数")

if __name__=='__main__':
    main()
