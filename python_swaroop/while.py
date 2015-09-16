#!/usr/bin/python
# Filename: while.py
import random

number=random.randint(0,9)
running=True
while running:
    try:
    	guess=int(raw_input('Enter an integer in [0-9]: '))
    except:
	continue
    if guess==number:
        print '\nCongratulations, You guessed it !\n'
        running=False
    elif guess<number:
        print 'It is a little higher than that'
    else:
        print 'It is a liitle lower than that'
#else:
#    print 'The while loop is over.'
#print 'Done'
