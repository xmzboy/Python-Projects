from random import *
n = randint(1, 100)
print('Добро пожаловать в числовую угадайку')
counter = 0
def is_valid(num):
    if num.isdigit() and 1 <= int(num) <= 100:
        return True
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
        return False
while 1:
    counter += 1
    user_num = input('Введите ваше число: ')
    if is_valid(user_num):
        if int(user_num) == n:
            print(f'Вы угадали, поздравляем! Количество попыток = {counter}')
            print('Если хотите сыграть ещё раз нажмите кнопку W. Если хотите закончить нажмите любую кнопку.')
            if input().lower() == 'w':
                counter = 0
                n = randint(1, 100)
                continue
            break
        elif int(user_num) > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Ваше число меньше загаданного, попробуйте еще разок')
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')