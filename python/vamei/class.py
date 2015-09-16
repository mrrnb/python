#!/usr/bin/python
#Filename: class.py

class Human(object):
	laugh="hahaha"
	kuqi="555"
	def show_laugh(self):
		print self.laugh
	def laugh_100th(self):
		for i in range(10):
			self.show_laugh()

#person=Human()
#person.show_laugh()
#print person.kuqi
#person.laugh_100th()

class Man(Human):
	jj="yes"
	xiong="no"
	def dajia(self):
		self.show_laugh()
		print "i can fight"

class Woman(Human):
	jj="no"
	xiong="yes"
	def maimeng(self):
		print self.kuqi
		print "i am mengmengda"


nan=Man()
nv=Woman()
nan.dajia()
nv.maimeng()
