from itertools import islice

num = 20
print(*islice((i for i in range(num + 1) if i % 2 == 1), num))




