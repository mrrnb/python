#!/usr/bin/python

file_name='query.txt'
f = file(file_name)
c = f.readlines()
running = True

while running:
    user_input = raw_input('Input sth to search: ')
    if len(user_input) == 0:
        continue
    for line in c:
        if user_input in line:
            print line
        elif user_input == 'quit':
            # running = False
            # break
            exit()
    else:
        print 'Can not Search the key value !'

