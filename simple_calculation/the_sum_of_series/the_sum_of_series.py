mult = 1
count = 0
summ = 0
while 1:
    n = int(input("Введите натуральное n = "))
    if not n < 1:
        break;
while count < n:
    count += 1
    k = count;
    while k > 0:
        mult *= count
        k -= 1
    summ += (1 / mult)
    mult = 1
print("Сумма:", summ)
