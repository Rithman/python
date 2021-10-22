import os
from collections import defaultdict

root_dir = os.getcwd()

f_list = defaultdict(int)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if os.stat(file).st_size < 100:
            f_list[100] += 1
        elif 100 <= os.stat(file).st_size < 1000:
            f_list[1000] += 1
        elif 1000 <= os.stat(file).st_size < 10000:
            f_list[10000] += 1
        elif 10000 <= os.stat(file).st_size < 100000:
            f_list[100000] += 1
        elif 100000 <= os.stat(file).st_size < 1000000:
            f_list[1000000] += 1
        elif 1000000 <= os.stat(file).st_size:
            f_list['10000000_and_more'] += 1

print(f_list)
