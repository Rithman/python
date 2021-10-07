def thesaurus(*args):
    result = {}
    for i in args:
        name, surname = i.split(' ')
        result.setdefault(surname[0], (name[0], list(filter(lambda n: n.startswith(name[0]), args))))
    print(result)


# Сдесь был сломан мой мозг. Код не рабочий. Точнее рабочий, но совсем не так как требуется.
# Прикрепил файл чтобы показать ход мыслей.
# Совсем не понял почему dict(filter(lambda n: n.startswith(name[0]), args)) не работает, а list работает
# (хотя бы запускается)

thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

# def thesaurus(*args):
#     result = {}
#     for i in args:
#         name, surname = i.split(' ')
#         result.setdefault(str(filter(lambda n: n.startswith(surname[0]), args)), (name[0], list(filter(lambda n: n.startswith(name[0]), i))))
#     print(result)
#
#
# thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
