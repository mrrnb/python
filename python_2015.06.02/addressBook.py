#!/usr/bin/python
#coding: utf8


msg = '''
		1. Add Information
		2. Display Information
		3. Delete Information
		4. Update Information
		5. Save
		6. Exit
'''

attr = '''
Which attribute do you want to update:
		1. name
		2. gender
		3. telphone
'''


#txl = [['name','gender','telphone']]
txl = []


def loadUser():
	import os
	if os.path.exists('user.db'):
		uFile = file('user.db','r')
		uContent = uFile.read()
		uFile.close()
		print uContent
		temp = uContent.split('\n')
		print temp
		for info in temp:
			txl.append(info.split(','))

	else:
		uFile = file('user.db','w')
		uFile.close()



def save():
	temp = []
	for info in txl:
		temp.append(','.join(info))
		s = '\n'.join(temp)
        fp = file('user.db','w')
        fp.write(s)
        fp.close()

def addUser():
	name = raw_input('NAME > ')
	gender = raw_input('GENDER > ')
	telphone = raw_input('TELPHONE > ')
	txl.append([name,gender,telphone])

def displayUser(dis_who='all'):
	if dis_who == 'all':
		for inf in txl:
			print ',\t'.join(inf)
	else:	
		for inf in txl:
			if inf[0] == dis_who:
				print ',\t'.join(inf)
			else:
				continue

def deleteUser():
	name = raw_input('Delete NAME > ')
	for i in txl:
		if i[0] == name:
			txl.remove(i)

def updateUser():
	name = raw_input('Update NAME > ')
	for i in txl:
		if i[0] == name:
			opt = raw_input(attr)
			if opt == '1':
				i[0] = raw_input('Please input new NAME > ')
			elif opt == '2':
				i[1] = raw_input('Please input new GENDER > ') 
			elif opt == '3':
				i[2] = raw_input('Please input new TELPHONE > ')
			else:
				print ''
			displayUser(i[0])
		else:
			continue	

loadUser()
while True:
	print msg
	try:
		op = int(raw_input('Please Select >>> '))
	except ValueError:
		print 'Input Eroor'
		continue
	op_dict = {	1 : addUser,
				2 : displayUser,
				3 : deleteUser,
				4 : updateUser,
				5 : save,
				6 : exit}
	if op <= 6 and op >= 1:
		op_dict[op]()
	else:
		continue
