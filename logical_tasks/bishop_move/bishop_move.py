x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
n = abs(x1 - x2)
m = abs(y1 - y2)
if n == m:
    print('YES')
else:
    print('NO')