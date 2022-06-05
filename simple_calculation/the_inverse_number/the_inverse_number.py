n2 = 0
while 1:
    n1 = int(input("Введите натуральное число: "))
    if not n1 < 1:
        break;
while n1 > 0:
	d = n1 % 10
	n1 = n1 // 10 
	n2 = n2 * 10 
	n2 = n2 + d 
print('Обратное число:', n2)
