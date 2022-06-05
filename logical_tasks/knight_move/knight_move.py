x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
n = abs(x1 - x2)
m = abs(y1 - y2)
if n == 1 and m == 2 or n == 2 and m == 1:
    print('YES')
else:
    print('NO')