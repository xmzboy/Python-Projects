n = int(input('Введите количество элементов массива: '))
arr = [0] * n
count = 0
for i in range (n):
    arr[i] = int(input('Введите элемент массива:\n'))
average = sum(arr) / n
for i in range (n):
    if average < arr[i]:
        count += 1
print(count)