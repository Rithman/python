import re

RE_EMAIL = re.compile('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$')


def email_parse(email_address):
    username, domain = email_address.split('@')[0], email_address.split('@')[1]
    assert RE_EMAIL.match(email_address), f'Wrong e-mail: {email_address}'
    return {"username": username, "domain": domain}


print(email_parse('someone@geekbrains.ru'))
