d = 2
while 1:
    print("Введите натурально x = "),
    x = int(input())
    if not x < 1:
        break;
if x == 1:
    print(x)
else:
    while x > 1:
        if x % d == 0:
            x = x / d
            print(d);
        else:
            d += 1