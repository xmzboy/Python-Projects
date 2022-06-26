digits = {1:'один', 2: 'два', 3: 'три', 4: 'четыре', 5:'пять', 6:'шесть', 7:'семь', 8:'восемь', 9:'девять',\
          10:'десять', 11:'одиннадцать', 12:'двенадцать', 13:'тринадцать', 14:'четырнадцать', 15:'пятнадцать',\
          16:'шестнадцать', 17:'семнадцать', 18:'восемнадцать', 19:'девятнадцать', 20:'двадцать', 30:'тридцать',\
          40:'сорок', 50:'пятьдесят', 60:'шестьдесят', 70:'семьдесят', 80:'восемьдесят', 90:'девяносто'}

# объявление функции
def number_to_words(num):
    num_str = ''
    for key in digits:
        if num == key:
            return digits[key]
    num_one = num // 10 * 10
    num_two = num % 10
    if len(str(num)) == 2 and num_one != 10 and num_two != 0:
        for key in digits:
            if num_one == key:
                num_str += digits[key]
        for key in digits:
            if num_two == key:
                num_str += ' ' + digits[key]
    return num_str


# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))