a, b, c = int(input()), int(input()), int(input())
minn, maxn = min(a, b, c), max(a, b, c)
print(max, a + b + c - minn - maxn, minn, sep = '\n')