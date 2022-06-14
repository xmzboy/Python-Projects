n = int(input())
for i in range(1, n // 2 + 1):
    print('*' * i)
for j in range(n // 2 + 1, 0, -1):
    print('*' * j)