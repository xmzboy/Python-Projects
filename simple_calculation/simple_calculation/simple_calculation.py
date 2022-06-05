a = float(input())
b = float(input())
f = 0
if a > 5:
    f = 3 * a ** 2
elif a > 0 and a <= 5 and b != 0:
    f = a / b
else:
    f = b + a - 1
print(f)