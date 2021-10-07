prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90, 70.01, 63, 39, 90.47, 29, 24, 42, 59.11]
print(id(prices))

# a.
for elem in prices:
    elem = (f'{elem: .2f}')
    elem = elem.replace('.', ' руб ')
    elem = elem.replace(elem, (elem + ' коп'))
    print(elem, end=', ')

print()

# b.
prices.sort()
print(prices)
print(id(prices))

# c.
prices_revert = sorted(prices, reverse=True)
print(prices_revert)

# d.
print(sorted(prices_revert[:5], reverse=True))
