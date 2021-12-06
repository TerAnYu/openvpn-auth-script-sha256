#!/usr/bin/python
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

in_user = sys.argv[1]
in_password = sys.argv[2]
in_password = hashlib.sha256(in_password.encode("utf-8")).hexdigest()
f = open(get_script_dir()+'/users.db', 'w+')

new_line = in_user + ":" + in_password

if os.path.getsize("users.db") > 0:
    f.write("\n" + new_line)
	f.close()
	sys.exit(0)
else:
    f.write(new_line)
	f.close()
	sys.exit(0)
