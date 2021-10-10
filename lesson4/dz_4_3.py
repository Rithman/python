from decimal import Decimal
from datetime import date
from requests import get, utils

cbr = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(cbr.headers)
content = cbr.content.decode(encoding=encodings)
cur_list = content.split('<Valute')


def currency_rates(currency):
    cur_date = date(day=int(cur_list[0][-43:-41]), month=int(cur_list[0][-40:-38]), year=int(cur_list[0][-37:-33]))
    for i in cur_list:
        cur_str = ''.join(i)
        if currency.upper() in cur_str:
            rub = Decimal(cur_str[-24:-19].replace(',', '.'))
            return rub, cur_date


if __name__ == '__main__':
    print(currency_rates('usd'))

    print(currency_rates('EUR'))
