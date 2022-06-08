n = int(input())
large, prelarge = -1, -1
for i in range(n):
    num = int(input())
    if num > large:
        prelarge = large
        large = num
    if num > prelarge and num < large:
        prelarge = num
print(large)
print(prelarge)