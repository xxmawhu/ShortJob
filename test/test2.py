#!/usr/bin/env python
import os
from ShortJob import MkMulJob

# get all files in the current directory
fileList = os.listdir(".")

# only need those file end with .C
scriptList = []
for f in fileList:
    if f.endswith(".C"):
        scriptList.append(f)

mk = MkMulJob.MkMulJob(["run.C"])
for i, f in enumerate(scriptList):
    input_value = [f[:-2]]
    print input_value
    mk.Make(i, [input_value])
