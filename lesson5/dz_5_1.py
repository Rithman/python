def num_sqrt(num):
    for i in range(num + 1):
        if i % 2 == 1:
            yield i


sqrt_20 = num_sqrt(20)
print(*sqrt_20)
print(next(sqrt_20))
