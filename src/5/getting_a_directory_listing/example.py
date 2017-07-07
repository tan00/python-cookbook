# Example of getting a directory listing

import os,sys
import os.path
import glob

def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

os.chdir( cur_file_dir() )


names = [name for name in os.listdir(cur_file_dir())
if os.path.isfile(os.path.join(cur_file_dir(), name))]




pyfiles = glob.glob('*.py')

# Get file sizes and modification dates
name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                for name in pyfiles]

for r in name_sz_date:
    print(r)

# Get file metadata
file_metadata = [(name, os.stat(name)) for name in pyfiles]
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)
