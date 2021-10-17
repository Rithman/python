import json
from itertools import zip_longest
from sys import argv

users_file_path = str(argv[1])
users = open(users_file_path, 'r', encoding='utf-8')
users_par = users.readlines()

users_par_clean = []
for line in users_par:  # очищаем ФИО от /n
    line_clean = line.strip()
    users_par_clean.append(line_clean)

hobby_file_path = str(argv[2])
hobby = open(hobby_file_path, 'r', encoding='utf-8')
hobby_par = hobby.readlines()

hobby_par_clean = []
for line in hobby_par:  # очищаем хобби от /n
    line_clean = line.strip()
    hobby_par_clean.append(line_clean)

result_dict = {}
for (i, j) in zip_longest(users_par_clean, hobby_par_clean):  # формируем словарь
    s, n, p = i.split(',')[0], i.split(',')[1], i.split(',')[2]
    h = j
    result_dict[f'{s} {n} {p}'] = h

users_hobby_file_path = str(argv[3])
with open(users_hobby_file_path, 'w', encoding='utf-8') as users_hobby:
    json.dump(result_dict, users_hobby)  # пишем словарь в файл .json

users.close()
hobby.close()

# Осталось не понятно как синтаксически правильно офрмить несколько with open.
# Вы как-то очень вскользь сказали про это на лекции, поэтому пока сделал по-простому.

