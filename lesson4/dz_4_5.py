from sys import argv
from utils import currency_rates

def show_surrency_rate(val):
    _, val = argv
    print(currency_rates(val))

if __name__ == '__main__':
    show_surrency_rate('gbp')