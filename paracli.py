#!/usr/bin/env python2
import multiprocessing
import subprocess
import sys
from multiprocessing.pool import ThreadPool
#
# The worker run_cmd launch a subprocess
# and wait for it to finish with communicate
#
def run_cmd(cmd):
    p = subprocess.Popen(cmd, shell=True)
    out, err = p.communicate()
    return 0
#
# Test if 3rd argument is an integer
# 
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
#
#
# Begin main
#
#
ncpu = multiprocessing.cpu_count()
#
# Managing exceptions
# TODO: clean this up
#
if not len(sys.argv)==3:
    sys.exit("Please call paracli.py with argument -k n with n the "+
    "number of process to use")
if not sys.argv[1]=="-k":
    sys.exit("Please call paracli.py with argument -k n with n the "+
    "number of process to use")
if not RepresentsInt(sys.argv[2]):
    sys.exit("Please call paracli.py with argument -k n with n the "+
    "number of process to use")
else:
    n=int(sys.argv[2])
if n==0:
    n=ncpu
elif n > ncpu:
    print "n is too high, you only have "+str(ncpu)+" cpu"
    print "n is set to "+str(ncpu)
    n=ncpu
#
# Open list of command
#
with open('sample_cli.list') as f:
    lines = f.readlines()
f.close()
#
# Create the pool of threads
#
pool = ThreadPool(n)
#
# Work its way though the list
#
for line in lines:
    pool.apply_async(run_cmd, (line,))
#
pool.close()
pool.join()
#

