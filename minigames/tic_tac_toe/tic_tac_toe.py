class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def set_symbol(self):
        try:
            user_choice = int(input(f'{self.name.title()}, please enter index: '))
            if user_choice < 0 or user_choice > 8:
                raise
        except:
            print('You should enter the number (0-8)')
            user_choice = self.set_symbol()
        return user_choice


class Game:
    def __init__(self):
        self.spot = ['_'] * 9

    def draw_spot(self, p):
        print(*self.spot[:3])
        print(*self.spot[3:6])
        print(*self.spot[6:])
        return self.__check(p)


    def __check(self, p):
        if any([all([p.symbol in x for x in self.spot[0:3]]), all([p.symbol in x for x in self.spot[3:6]]),
                all([p.symbol in x for x in self.spot[6:9]]), all([p.symbol in x for x in self.spot[0:9:3]]),
                all([p.symbol in x for x in self.spot[1:9:3]]), all([p.symbol in x for x in self.spot[2:9:3]]),
                all([p.symbol in x for x in self.spot[0:9:4]]), all([p.symbol in x for x in self.spot[2:7:2]])]):
            print(f'Congratulations! {p.name.title()} you are win!')
            return True
        return False


def choice(p):
    p_choice = p.set_symbol()
    if game.spot[p_choice] != '_':
        print('You should enter correct index')
        p_choice = p.set_symbol()
    game.spot[p_choice] = p.symbol


game = Game()

name1 = input('Player1, enter your name: ')
name2 = input('Player2, enter your name: ')

p1 = Player(name1, 'x')
p2 = Player(name2, 'o')

move_counter = 0

while True:
    if move_counter % 2 == 0:
        choice(p1)
        if game.draw_spot(p1):
            break
    else:
        choice(p2)
        if game.draw_spot(p2):
            break

    if '_' not in game.spot:
        print("It's draw!")
        break
    move_counter += 1
