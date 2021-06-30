__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
cur_path = os.getcwd()
print(cur_path)
cache_path = os.path.join(cur_path, 'files', 'cache')
zip_path = os.path.join(cur_path, 'files', 'data.zip')

from zipfile import ZipFile
import shutil

def clean_cache():
    path = cache_path
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(cache_path)
    return 1

def cache_zip(path_zipfile, path_cache_dir):
    with ZipFile(path_zipfile, 'r') as zipObj:
        zipObj.extractall(path=path_cache_dir)
    return 1

def cached_files():
    cur_path = os.path.abspath('.')
    file_list = []
    for i in os.listdir(cache_path):
        x = os.path.join(cache_path, i)
        print(x)
        if os.path.isfile(x):
            file_list.append(x)
    return file_list

def find_password(path_password_list):
    for i in path_password_list:
        file = open(i, 'r')
        for line in file:
            if 'password' in line: 
                return line[line.find(' ')+1:].rstrip()


clean_cache()
# print(os.listdir())
cache_zip(zip_path, cache_path)
path_password_list = cached_files()
print(path_password_list)

find_password(path_password_list)
result = find_password(path_password_list) 
print(result)