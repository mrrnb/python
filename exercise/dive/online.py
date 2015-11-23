#!/usr/bin/env /python3

line_number = 0
with open('examples/people_name.txt',encoding='utf-8',mode='r') as a_file:
    for line in a_file.readlines():
        line_number += 1
        print('{0:>4} {1}'.format(line_number,line.rstrip()))
