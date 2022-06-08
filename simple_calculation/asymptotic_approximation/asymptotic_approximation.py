from math import log
n = int(input())
total = 0
for i in range(1, n + 1):
    total += 1 / i
total -= log(n)
print(total)