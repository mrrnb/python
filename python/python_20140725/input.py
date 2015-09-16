#!/usr/bin/python

this_year = 2014
name = raw_input('please input you name: ').strip()
age = int(raw_input('How old are you : '))
sex = raw_input('Please input your sex: ')
dep = raw_input('Which department: ')

#print "\n","Hello,",name
#print "you are ",age,"years old!"
#print "So you were born in: ",this_year-age

message = '''
Infomation of the company :
    name = %s
    born = %d
    sex  = %s
    dep  = %s
    ''' %(name, this_year-age, sex, dep)
print message

if age < 21:
    print "Congratulations! you've got half day's public holiday!"
elif age == 21:
    print "As you are at the right age, i am about to give 2 hours holiday!"
else:
    print "Sorry, you are too old to have this holiday! get back to work!"
