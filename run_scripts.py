#!/usr/bin/python


import os
import sys
import time
import os.path
import subprocess

def get_cmd_file(rootdir):
    fnlist = []
    for parent,dirnames,filenames in os.walk(rootdir):
        for filename in filenames:
            the_file = os.path.join(parent,filename)
            fnlist.append(the_file)
    return fnlist

def run_cmd(rootdir):
    for fn in get_cmd_file(rootdir):
        command = "/bin/sh %s "%fn
        print "===>",command
        subprocess.call(["/bin/sh",fn])


if __name__ == "__main__":
    rootdir = "/scripts"
    st = int(sys.argv[1])
    if os.getenv('RSYNC_RUN_INTERVAL'):
        try:
            st = int(os.getenv('RSYNC_RUN_INTERVAL'))
        except:
            pass
    print "run interval sec %d"%st
    run_cmd(rootdir)
    time.sleep(st)
