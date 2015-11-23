#!/usr/bin/python
#Filename: class.py

class MyClass:
    count=0
    name='MyClassName'
    def __init__(self,name):
        self.name=name
        print "MyClass name is %s\nMyMethod name is %s"%(MyClass.name,self.name)
    def GetInfo(self,id):
        self.id=id
        print "get information by %s."%self.id


p=MyClass('MyMethodName')
p.GetInfo("self")
