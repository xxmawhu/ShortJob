#!/usr/bin/env python
# ====================================================
#   Copyright (C)2019 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : setup.py
#   Created Time  : 2019-09-24 10:51
#   Last Modified : 2019-09-29 12:09
#   Describe      :
#
# ====================================================

from setuptools import setup
from setuptools import find_packages
import core
import subprocess
import sys
import os
setup(
    name='ShortJob',
    version='1.1',
    author='Xin-Xin Ma',
    packages=find_packages(),
    project_urls={
    'Source': 'https://github.com/xxmawhu/ShortJob',
	}
)
