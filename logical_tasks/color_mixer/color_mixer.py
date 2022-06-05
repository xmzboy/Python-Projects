a, b = input(), input()
mix = a + b
if mix == 'красныйкрасный' or mix == 'синийсиний' or mix == 'желтыйжелтый':
    print(a)
else:
    if mix == 'красныйсиний' or mix == 'синийкрасный':
        print('фиолетовый')
    elif mix == 'красныйжелтый' or mix == 'желтыйкрасный':
        print('оранжевый')
    elif mix == 'синийжелтый' or mix == 'желтыйсиний':
        print('зеленый')
    else:
        print('ошибка цвета')