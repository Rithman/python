import os
from distutils.dir_util import copy_tree

src = os.path.join(os.getcwd(), 'my_project')

try:
    all_templates_dir = os.mkdir('my_project/templates')
except (FileExistsError, PermissionError) as e:
    print(f'Ошибка: {e}')

for root, dirs, files in os.walk(src):
    for dir in dirs:
        if 'templates' in dir:
            templates_dir = os.path.abspath(os.path.join(root, dir))
            try:
                copy_tree(templates_dir, os.path.join(src, 'templates'))
            except (FileExistsError, PermissionError) as d:
                print(f'Ошибка: {d}')

"""
Я категорически не понимаю:
1. Почему код работает в таком виде. templates_dir это же папки templates, а не подпапки в них (authapp и mainapp),
которые и нужно копировать. Я пытался скопировать элементы и templates, и получал копирование только файлов html.
Не понятна фраза из методички: "обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён)". Папки играют роль пространства имен? Как это?
2. Почему работает с distutils.dir_util.copy_tree и не работает с shutils.copytree.
Если объясните в двух словах, хотя бы при разборе ДЗ на сл. занятии, буду очень признателен.
"""
