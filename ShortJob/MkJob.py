#!/usr/bin/env python
# ====================================================
#   Copyright (C)2019 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : MkJob.py
#   Created Time  : 2019-10-30 18:28
#   Last Modified : 2019-10-30 18:28
#   Describe      :
#
# ====================================================

import os

class MkJob:
    def __init__(self, cpp="fit.cxx"):
        self._cpp = cpp
        self._cwd = os.getcwd()
    def Make(self, index, var=[]):
        if type(var) != type([]):
            print("Error: the second var type should be 'List'")
        f=open("job_%d.sh"%(index),'w')
        f.write("cd %s\n"%(self._cwd))
        f.write("cd .. \n")
        f.write("root -l -b -q %s"%(self._cpp))
        if len(var)==0: 
            f.write(">%s/log%d"%(self._cwd.split("/")[-1],index))
            f.close()
            return 
        s = r'\('
        jj = 0
        for i in var:
            if type(i)==type("hello") :
                s += '\\\"%s\\\"'%(i)
            else:
                s += str(i)
            jj += 1
            if jj == len(var):
                s += r"\)"
            else:
                s += ","
        f.write(s)
        f.write(">%s/log%d"%(self._cwd.split("/")[-1],index))
        f.close()
