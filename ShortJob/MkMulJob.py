#!/usr/bin/env python
# ====================================================
#   Copyright (C)2019 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : MkMulJob.py
#   Created Time  : 2019-10-30 18:29
#   Last Modified : 2019-10-30 18:29
#   Describe      :
#
# ====================================================

import os
class MkMulJob:
    def __init__(self, cppList=["fit.cxx"]):
        self._cppList = cppList
        self._cwd = os.getcwd()

    def Make(self, indx, varList=[], logName=[]):
        if len(logName) != len( self._cppList) and len(logName)>0:
            print("check the length")
            return 
        if len(logName)==0:
            for i in self._cppList:
                logName.append(i.split('.')[0])

        f=open("job_%06d.sh"%(indx),'w')
        f.write("cd %s\n"%(self._cwd))
        f.write("cd .. \n")
        for i in range(len(varList)):
            f.write(self.GetCommands(indx, self._cppList[i],varList[i], logName[i]))
            #print(self.GetCommands(index, self._cppList[i],varList[i], logName[i]))
        f.close()

    def GetCommands(self,index, cpp, var=[], logName = "txt"):
        commands = " "
        commands += "root -l -b -q '%s"%(cpp)
        if len(var)==0: 
            commands +=\
                ">%s/log%d.%s;\n"%(self._cwd.split("/")[-1],index,\
                logName)
            return commands
        s = "("
        jj = 0
        for i in var:
            if type(i)==type("hello"):
                s += '"%s"'%(self.Str(i))
                #s += '\\\"%s\\\"'%(self.Str(i))
            else:
                s += str(i)
            jj += 1
            if jj == len(var):
                s += ")'"
                #s += r"\)"
            else:
                s += ","
        commands += s
        commands +=\
                ">%s/log%d.%s;\n"%(self._cwd.split("/")[-1],index,\
                logName)
        return commands
    def Str(self,s):
        return s
        st = ""
        for i in s:
            print i
            if i=="<" or i==">" or i == "|":
                st += '\\'+i
            else:
                st += i
        return st
