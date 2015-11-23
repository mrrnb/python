#!/usr/bin/env python

from UserDict import UserDict

class FileInfo(UserDict):
    "store file metadata"
    def __init__(self,filename=None):
        UserDict.__init__(self)
        self['name']=filename
