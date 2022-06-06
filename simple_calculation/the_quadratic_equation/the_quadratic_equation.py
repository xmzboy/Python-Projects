from math import sqrt
a, b, c = float(input()), float(input()), float(input())
D = b * b - 4 * a * c
if D > 0:
    x1, x2 = (-b + D**0.5) / (2 * a), (-b - D**0.5) / (2 * a)
    print(min(x1, x2), max(x1, x2), sep='\n')
elif D == 0:
    print(-b / (2 * a))
else:
    print('Нет корней')