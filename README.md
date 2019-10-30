# ShortJob
## Install
```sh
python setup.py install
```
You can also install it into your local directory by
```sh
python setup.py install --user
```
## Usage
Make a bash file 
```py
#!/usr/bin/env python
from ShortJob import MkMulJob
mk = MkMulJob.MkMulJob(["cut.cxx", "fit.cxx"])
cut_argv = [1.1, 1.2]
fit_argv = ["mass < 2.4"]
mk.Make(1, [cut_argv, fit_argv])
```
