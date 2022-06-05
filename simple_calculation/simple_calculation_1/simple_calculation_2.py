a = float(input())
b = float(input())
if a > 0 and b > 0:
    c = (a + b) / 2
    if a < b:
        b = c
    else: 
        a = c
elif a < 0 and b < 0:
    if a < b:
        a = -a
    elif a > b:
        b = -b
elif (a > 0 and b < 0) or (a < 0 and b > 0):
    a = 2 * a
    b = 2 * b
print(a, b)
 
