num = int(input())
if 0 <= num < 37:
  if (0 < num <11 or 18 < num < 29) and num % 2 or (10 < num < 19 or 28 < num < 37) and num % 2 == 0:
    print('красный')
  elif num == 0:
    print('зеленый')
  else:
    print('черный')
else:
  print('ошибка ввода')