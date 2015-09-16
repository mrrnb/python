#!/usr/bin/python


def u_xf(u_name):

    if u_name == 'ezreal':
        asset = 15000

    f_name = 'shopping.txt'
    f = open(f_name)
    shop_list = {}

    for line in f.readlines():
        li = line.split()
        shop_list[int(li[0])] = [li[1],int(li[2])]
    print shop_list
    f.close()


    mini_price = min(i[1] for i in shop_list.values())

    if asset >= mini_price:
        pass
    else:
        print 'You can not buy anything'

    while True:
      for i in shop_list.keys():
        print '%s>\t%s\t%s'%(i,shop_list[i][0],shop_list[i][1])
      try:
        if asset >= mini_price:
            buy = int(raw_input('Press 0 to return or Choose one: '))
        else:
            print 'Sorry, You can not buy anything !'
            buy = int(raw_input('Press 0 to return: '))
      except ValueError:
        print 'Please input a number !\n'
        continue
      if buy in shop_list:
        print shop_list[buy] 
        if asset >= shop_list[buy][1]:
            asset = asset-shop_list[buy][1]
            print 'asset left %s\n'%(asset)
        else:
            print 'Sorry, You can not pay it !!\n' 
      elif buy == 0:
          break
      else:
          print 'No good for you !\n'
