n, summ = int(input()), 0
for i in range(1, n + 1):
    summ += (-1)**(i+1) * i
print(summ)