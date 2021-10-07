def thesaurus(*args):
    result = {}
    for name in args:
        result.setdefault(name[0], list(filter(lambda i: i.startswith(name[0]), args)))
    print(result)


thesaurus("Иван", "Мария", "Петр", "Илья")

