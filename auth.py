#!/usr/bin/python3.8
import sys
import hashlib
import os
import inspect

def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False): # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)
#print(get_script_dir())

tmpFile = open(sys.argv[1], 'r')
lines = tmpFile.readlines()
input_user = lines[0].strip()
input_pass = lines[1].strip().encode("utf-8")
input_pass = hashlib.sha256(input_pass).hexdigest()
f = open(get_script_dir()+'/users.db', 'r')
for line in f:
    line = line.strip()
    array = line.split(":")
    user = array[0]
    password = array[1]
    if user == input_user:
        if password == input_pass:
            print("auth success! ")
            f.close()
            sys.exit(0)
print("epic fail")
f.close()
sys.exit(1)
