#!/usr/bin/env python

class UserDict():
    def __init__(self,dict=None):
        self.data={}
        if dict is not None:
            self.update(dict)

    def clear(self):
        self.data.clear()
    
    def copy(self):
        if self.__class__ is UserDict:
            return UserDict(self.data)
        import copy
        return copy.copy(self)
    def keys(self):
        return self.data.keys()
    def items(self):
        return self.data.items()
    def values(self):
        return self.data.values()
