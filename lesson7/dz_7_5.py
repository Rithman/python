import os
import json
from collections import defaultdict

root_dir = os.getcwd()
f_list = defaultdict(list)
count_100 = 0
ext_100_list = []
count_1000 = 0
ext_1000_list = []
count_10000 = 0
ext_10000_list = []
count_100000 = 0
ext_100000_list = []

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if os.stat(file).st_size < 100:
            count_100 += 1
            ext_100 = file.rsplit('.', maxsplit=1)[-1].lower()
            if ext_100_list.count(ext_100) == 0:
                ext_100_list.append(ext_100)
            f_list[100] = f'({count_100}, {ext_100_list})'
        elif 100 <= os.stat(file).st_size < 1000:
            count_1000 += 1
            ext_1000 = file.rsplit('.', maxsplit=1)[-1].lower()
            if ext_1000_list.count(ext_1000) == 0:
                ext_1000_list.append(ext_1000)
            f_list[1000] = f'({count_1000}, {ext_1000_list})'
        elif 1000 <= os.stat(file).st_size < 10000:
            count_10000 += 1
            ext_10000 = file.rsplit('.', maxsplit=1)[-1].lower()
            if ext_10000_list.count(ext_10000) == 0:
                ext_10000_list.append(ext_10000)
            f_list[10000] = f'({count_10000}, {ext_10000_list})'
        elif 10000 <= os.stat(file).st_size < 100000:
            count_100000 += 1
            ext_100000 = file.rsplit('.', maxsplit=1)[-1].lower()
            if ext_100000_list.count(ext_100000) == 0:
                ext_100000_list.append(ext_100000)
            f_list[100000] = f'({count_100000}, {ext_100000_list})'

print(f_list)

with open('files_list.json', 'w', encoding='utf-8') as f:
    json.dump(f_list, f)