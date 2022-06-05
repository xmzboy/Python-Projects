from math import*

n = 1
while 1:
    x = float(input('Введите вещественное число с разделителем точкой x='))
    if not x <= 1:
        break;
summ = a = (x - 1) / x;
while a > 1e-5:
    n += 1
    a *= (n * x - n - x + 1) / (n * x)
    summ += a
f = log(x)
print("Сумма:", summ)
print("Проверка", f)