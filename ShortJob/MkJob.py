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
from ShortJob import MkMulJob


class MkJob(MkMulJob):
    def __init__(self, cpp="fit.cxx"):
        super(MkJob, self).__init__()
        self._cpp = cpp
        self._cwd = os.getcwd()

    def SetTarget(self, cpp):
        self._cpp = cpp

    def Make(self, index, var=[]):
        tail = self._cpp.split('.')[0]
        logName = "log_{}.{}".format(index, tail)
        MkMulJob.Make(index, [var], [logName])
