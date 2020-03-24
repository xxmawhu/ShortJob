
# ShortJob

This package is consistent of four module, i.e. `command`, `MkJob`, `MkMulJob`,
`GetResult`.
* command Specify each fileType with one execute command, such as
> .sh -> bash
> .C -> root -l -b -q
* MkMulJob generate a massive bash scripts with input tasks
Example:
```bash
cd /home/maxx/work/GitHub/ShortJob/test
cd ..
root -l -b -q 'run.C(3.14,2.3,"a")' > test/log1.run
python test.py a b c > test/log1.test
bash run.sh a > test/log1.run
```
* MkJob generate a massive bash scripts with only one task
* GetResult pick the result of interest from the log file.



# ShortJob.MkMulJob


## MkMulJob
```python
MkMulJob()
```
generate a bash script contains only more than one task
Example: the task is a list
tasks = ["buy.csh", "mix.py", "cock.cxx", "sell.sh"]
and the args for each task is
[(0.1, 2, 0.3, 4), ("a", "b"), (2, "cack"), (3.2)]
the recommend style is
mkjob = MkMulJob(tasks)
mkjob.Make(0, [(0.1, 2, 0.3, 4), ("a", "b"), (2, "cack"), (3.2)])


# ShortJob.MkJob


## MkJob
```python
MkJob()
```
Make job with only one task, inherited from MkMulJob


# ShortJob.GetResult


## GetResult
```python
GetResult()
```

Reqiure ROOT
How:
    The program tries to find any pattern "name value" in the log file
    For example:
        alpha 0.321
    In this case, the "alpha" is assigned to be 0.021.
        beta 0.01 0.321 +/- 0.001
    In this case, the "beta" is assigned to be 0.321 +/- 0.001, while
    0.001 is the uncertainty
    * Warrn: the new value will overwrite the old one.
Example:
    info = GetResult.("fit.log")
    fcn = info.FCN()
    tmpArgValue = info.GetVal("alpha")


# ShortJob.command


## MyConfigParser
```python
MyConfigParser()
```
set ConfigParser options for case sensitive.

## initConfig
```python
initConfig(execommand)
```
init the ConfigParser file, the commands is stored in ~/.ShortJob/command
Args:
   execommand(dir): take the file type as key and the command as value
Returns:
    void

