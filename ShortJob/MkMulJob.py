#!/usr/bin/env python
# ====================================================
#   Copyright (C)2019 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : MkMulJob.py
#   Created Time  : 2019-10-30 18:29
#   Last Modified : 2019-12-30 20:16
#   Describe      :
#
# ====================================================
import os


class MkMulJob(object):
    def __init__(self, cppList=["fit.cxx"]):
        self._cppList = cppList
        self._cwd = os.getcwd()

    def Make(self, indx, varList=[], logName=[]):
<<<<<<< HEAD
        if len(logName) != len( self._cppList) and len(logName)>0:
=======
        if len(logName) != len(self._cppList) and len(logName) > 0:
>>>>>>> bd2a9fb9bfb93aff72c2a72cc001acb8466ec1d0
            print("check the length")
            return
        if len(logName) == 0:
            for i in self._cppList:
                logName.append(i.split('.')[0])

<<<<<<< HEAD
        f=open("job_%d.sh"%(indx),'w')
        f.write("cd %s\n"%(self._cwd))
=======
        f = open("job_%d.sh" % (indx), 'w')
        f.write("cd %s\n" % (self._cwd))
>>>>>>> bd2a9fb9bfb93aff72c2a72cc001acb8466ec1d0
        f.write("cd .. \n")
        for i in range(len(varList)):
            f.write(
                self.GetCommands(indx, self._cppList[i], varList[i],
                                 logName[i]))
        f.close()

    def GetCommands(self, index, cpp, var=[], logName="txt"):
        commands = " "
<<<<<<< HEAD
        commands += "root -l -b -q '%s"%(cpp)
        if len(var)==0: 
            commands +=\
                ">%s/log%d.%s;\n"%(self._cwd.split("/")[-1],index,\
                logName)
=======
        commands += "root -l -b -q '%s" % (cpp)
        if var:
            commands += ">>%s/log%d.%s;\n" % (self._cwd.split("/")[-1],
                                              index, logName)
>>>>>>> bd2a9fb9bfb93aff72c2a72cc001acb8466ec1d0
            return commands
        s = "("
        jj = 0
        for i in var:
            if isinstance(i, str):
                s += '"%s"' % (self.Str(i))
            else:
                s += str(i)
            jj += 1
            if jj == len(var):
                s += ")'"
            else:
                s += ","
        commands += s
<<<<<<< HEAD
        commands +=\
                ">%s/log%d.%s;\n"%(self._cwd.split("/")[-1],index,\
                logName)
=======
        commands += ">>%s/log%d.%s;\n" % (self._cwd.split("/")[-1], index,
                                          logName)
>>>>>>> bd2a9fb9bfb93aff72c2a72cc001acb8466ec1d0
        return commands

    def Str(self, s):
        return s
        st = ""
        for i in s:
            print(i)
            if i == "<" or i == ">" or i == "|":
                st += '\\' + i
            else:
                st += i
        return st
