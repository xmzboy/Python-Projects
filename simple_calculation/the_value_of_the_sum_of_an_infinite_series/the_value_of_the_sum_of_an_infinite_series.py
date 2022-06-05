from math import*
summ = 0
r = 0
si = 1
i = 0
while 1:
    a = float(input("Введите вещественное число с разделителем точкой a = "))
    if not a <= 0:
        break;
while 1:
    x = float(input("Введите вещественное число с разделителем точкой 0.1<=x<=1 x = "))
    if not (x > 1  or x < 0.1):
        break;
r = x * log(a)
while(fabs(si) >= (1e-4)):
    summ += si
    i += 1
    si = si * r / i
f = a ** x
print("Сумма:", summ)
print("Проверка:", f);
