res = 1
while True:
    print("Введите натуральное число")
    num = int(input())
    if not(num < 1):
        break;
for a in range(1, num + 1):
    if(a % 2):
        res *= (a + 1.0) / a
    else:
        res *= a / (a + 1.0)
print(res)
