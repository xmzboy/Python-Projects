eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
l = list()
act = ''

def solve(alphabet_upper, alphabet_lower, user_str, k):
    result = list()
    for i in range(len(user_str)):
        exitFlag = False
        for j in range(len(alphabet_upper)):
            if user_str[i] == alphabet_upper[j]:
                result.append(alphabet_upper[(j + k) % len(alphabet_upper)])
                exitFlag = True
            elif user_str[i] == alphabet_lower[j] and not exitFlag:
                result.append(alphabet_lower[(j + k) % len(alphabet_lower)])
                exitFlag = True
            elif user_str[i] not in alphabet_lower and user_str[i] not in alphabet_upper and not exitFlag:
                result.append(user_str[i])
                exitFlag = True
        if exitFlag:
            continue
    return result

def resolve(alphabet_upper, alphabet_lower, user_str, k):
    result = ''
    if k == 0:
        for i in range(len(alphabet_upper)):
            k = i
            result = (solve(alphabet_upper, alphabet_lower, user_str, k))
            print('Возможный текст = ', *result, sep='')
    else:
        result = solve(alphabet_upper, alphabet_lower, user_str, k)
        print(*result, sep='')

while act not in ['1', '2']:
    act = input('Если вы хотите зашифровать строку введите 1. Для дешифровки введите 2. ')
if act == '1':
    user_str = input('Введите строку которую хотите зашифровать: ')
    k = int(input('Введите сдвиг: '))
    alp = ''
    while alp not in ['1', '2']:
        alp = input('Выберите алфавит ввода. Нажмите 1 если алфавит русский или нажмите 2 если английский: ')
    if alp == '1':
        l = solve(rus_upper_alphabet, rus_lower_alphabet, user_str, k)
    else:
        l = solve(eng_upper_alphabet, eng_lower_alphabet, user_str, k)
    print(*l, sep='')
else:
    user_str = input('Введите строку которую хотите расшифровать: ')
    known = ''
    while known not in ['1', '2']:
        known = input('Если вы знаете сдвиг введите 1, если нет, то введите 2: ')
    if known == '1':
        k = int(input('Введите сдвиг: '))
    else:
        k = 0
    alp = ''
    while alp not in ['1', '2']:
        alp = input('Выберите алфавит ввода. Нажмите 1 если алфавит русский или нажмите 2 если английский: ')
    if alp == '1':
        resolve(rus_upper_alphabet, rus_lower_alphabet, user_str, k)
    else:
        resolve(eng_upper_alphabet, eng_lower_alphabet, user_str, k)