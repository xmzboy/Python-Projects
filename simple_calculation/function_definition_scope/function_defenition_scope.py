from math import*

a = float(input())
b = float(input())
if (sin(a) <= 1 and sin(a) >= -1) and b != 0 and (b - a) * (b - a) * exp(tan(a / b)) != 0:
    D = (-sin(a) + sqrt(sin(a) * sin(a) + 12 * fabs(log(fabs(b))))) / ((b - a) * (b - a) * exp(tan(a / b)))
    print(D)
else:
    print("Не принадлежит ООФ")