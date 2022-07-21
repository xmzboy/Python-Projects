from random import choice
choise_list = ['r', 's', 'p']
def is_valid():
    user_choice = input('Enter your choise: ')
    while user_choice.lower() not in ['r', 's', 'p']:
        user_choice = input('Please enter the correct answer (r, s, p): ')
    return user_choice

while 1:
    user_choice = is_valid()
    computer_choise = choice(choise_list)
    if user_choice == computer_choise:
        print('Draw. Your opponent has made a wish', computer_choise)
    elif user_choice + computer_choise in ('pr', 'rs', 'sp'):
        print('Victory. Your opponent has made a wish', computer_choise)
    else:
        print('Defeat. Your opponent has made a wish', computer_choise)
    cont = input('If you want to continue game please press W: ')
    if cont.lower() != 'w':
        break