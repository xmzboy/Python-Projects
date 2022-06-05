#guess = int(input('Введите целое число : '))
def arifmetic ( a = int(input('Введите 1-е число ')),b = int(input("Введите 2-е число ")),c = input("Ввeдите символ ")):
    if c == '+':
        return (a + b)
    elif c == '/':
        return (a / b)
    elif c == '*':
        return (a * b)
    elif c == '-':
        return (a - b)
    else:
        return print ('Незвестная операция')
print (arifmetic ())