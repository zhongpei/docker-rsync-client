#!/usr/bin/python


import os
import sys
import time





import os.path


def get_cmd_file(rootdir):
    fnlist = []
    for parent,dirnames,filenames in os.walk(rootdir):
        for filename in filenames:
            the_file = os.path.join(parent,filename)
            fnlist.append(the_file)
    return fnlist

def run_cmd(rootdir,sleep_sec):
    while True:
        for fn in get_cmd_file(rootdir):
            command = "/bin/sh %s"%fn
            print command
            os.system(command)
        time.sleep(sleep_sec)


if __name__ == "__main__":
    rootdir = "/scripts"
    sleep_sec = int(sys.argv[1])
    run_cmd(rootdir,sleep_sec)
