import os

dir_tree = {'my_project': {'settings': [], 'mainapp': [], 'adminapp': [], 'authapp': []}}

for key, val in dir_tree.items():
    if not os.path.exists(key):
        for k, v in val.items():
            path = os.path.join(key, k)
            os.makedirs(path)
    else:
        print(f'Папка {key} уже существует')
