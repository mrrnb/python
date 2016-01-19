#!/usr/bin/env python
#coding: utf-8
'''
【程序23】 
题目：打印出如下图案（菱形）

   *
  ***
 *****
*******
 *****
  ***
   *
1.程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重
　　　　　　for循环，第一层控制行，第二层控制列。 
2.程序源代码： 
'''
from sys import stdout

n=int(raw_input('Input a number: '))

for i in range(n):
    for j in range(n - i ):
        stdout.write('  ')
    for k in range(2 * i + 1):
        stdout.write('8 ')
    print

for i in range(n-1):
    for j in range(i + 2):
        stdout.write('  ')
    for k in range(2 * n - 2 * i - 3):
        stdout.write('8 ')
    print
