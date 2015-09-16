#!/usr/bin/python

from u_xf import u_xf

def u_cx(u_name):
    print 'Welcome %s'%u_name

#def u_xf(u_name):
#    pass

def u_qk(u_name):
    pass

def u_hk(u_name):
    pass

running = False
uc_position = 15000
err_count = 0
u_name = ''
dic_menu = {
        1 : u_cx,
        2 : u_xf,
        3 : u_qk,
        4 : u_hk
        }

while True:
    u_name = raw_input('USEENAME: ')
    u_code = raw_input('PASSWORD: ')
    if u_name == 'ezreal' and u_code == 'osatmnzn':
        running = True
        break
    else:
        print 'Account Password Error !!!'
        err_count += 1
        if err_count == 3:
            exit()

while running:
    try:
        u_choose = int(raw_input('1. cx\t2. xf\n3. qk\t4. hk\t 0. exit\n#### '))
    except ValueError:
        print 'Input Error'
        continue
    if u_choose >= 1 and u_choose <= 4:
        dic_menu[u_choose](u_name)
    elif u_choose == 0:
        exit()
    else:
        print 'Input Error'

