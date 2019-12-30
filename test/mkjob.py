#!/usr/bin/env python
import sys
sys.path.append("/home/maxx/work/GitHub/ShortJob")

from ShortJob import MkMulJob
target = ['getp4.cxx', 'fit.cxx']
mk = MkMulJob.MkMulJob(target)
argv1 = ["./dat/001.dat"]
argv2 = ["./dat/PHSP.dat", "Data.dat", "out2.root"]
mk.Make(1, [argv1, argv2])
