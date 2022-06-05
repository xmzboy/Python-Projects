month = int(input())
if (month % 2 == 1 and month < 8) or (month % 2 == 0 and month > 7):
    print('31')
elif month == 2:
    print('28')
else:
    print('30')