from random import *
digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
same_pun = 'il1Lo0O'

def valid_symbols(add_digits, add_upper_literals, add_lower_literals, add_symbols, add_same_symbols):
    valid = ['yes', 'да', 'д', 'y']
    result = ''
    if add_digits in valid:
        result += digits
    if add_upper_literals in valid:
        result += uppercase_letters
    if add_lower_literals in valid:
        result += lowercase_letters
    if add_symbols in valid:
        result += punctuation
    if add_same_symbols not in valid:
        result += same_pun
    return result

def generate_pass(n, pass_len, chars):
    l = list()
    result = ''
    for i in range(n):
        for j in range(pass_len):
            result += choice(chars)
        l.append(result)
        result = ''
    return l

n = int(input('Введите количество паролей которое вы хотите сгенерировать: '))
pass_len = int(input('Введите длину пароля: '))
add_digits = input('Включать ли цифры в пароль: ')
add_upper_literals = input('Включать ли ПРОПИСНЫЕ буквы в пароль: ')
add_lower_literals = input('Включать ли строчные буквы в пароль: ')
add_symbols = input('Включать ли символы в пароль: ')
add_same_symbols = input('Исключать похожие символы из пароля (Пример: 1ilLoO0): ')
chars = valid_symbols(add_digits, add_upper_literals, add_lower_literals, add_symbols, add_same_symbols)

print(*generate_pass(n, pass_len, chars), sep='\n')