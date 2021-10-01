cubes_list = []
i_sum = 0
total_sum = 0

for i in range(1, 1001):
    if i % 2 == 1:
        cubes_list.append(i ** 3)

# a.
for i in cubes_list:
    i_sum = 0
    tmp = i
    while i > 0:
        digit = i % 10
        i_sum = i_sum + digit
        i = i // 10
    if i_sum % 7 == 0:
        total_sum += tmp

print(total_sum)

# b, c.
total_sum = 0

for i in cubes_list:
    i += 17
    i_sum = 0
    tmp = i
    while i > 0:
        digit = i % 10
        i_sum = i_sum + digit
        i = i // 10
    if i_sum % 7 == 0:
        total_sum += tmp

print(total_sum)
