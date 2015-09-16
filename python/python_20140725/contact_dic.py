#!/usr/bin/python

f_name = 'contact_list.txt'
dic = {}
column_name = ['id','name','dep','phone']
print column_name

f = file(f_name)
for line in f.readlines():
    key = line.split()[0]
    dic[key] = line.split()[1:]
f.close()

while True:
    print '''Please choose below option to proceed:
    1. modify
    2. search
    '''
    try:
        option = int(raw_input('Please choose one: '))
    except ValueError:
        print 'only integer can be accepted: '
        continue
    if option == 1:
        li_op = raw_input('[e.g: update dep to HR for id 1 ]#: ').strip().split()
        if li_op[0] == 'update' and li_op[2] == 'to' and li_op[4] == 'for' and li_op[5] == 'id':
            li_id = li_op[-1]
            if dic.has_key(li_id):
                modify_id = column_name.index(li_op[1])-1
                print li_id+'   '+' '.join(dic[li_id])
                dic[li_id][modify_id] = li_op[3]
                print li_id+'   '+' '.join(dic[li_id])+'\n'
                f = file(f_name,'w')
                for k,v in dic.items():
                    line = '%s   %s\n'%(k,' '.join(v))
                    print line,
                    f.write(line)
                    f.flush()
                f.close()
                exit()
            else:
                print 'no id'
            
        else:
            print 'Input Error'
    elif option == 2:
        pass
    else:
        print 'Input Error'
        break
