src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [val for i, val in enumerate(src) if src[i] > src[i-1] and i != 0]

print(*result)
