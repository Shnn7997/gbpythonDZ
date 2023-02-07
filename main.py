day_n = int(input('Введите номер дня недели: '))
if 6 <= day_n <= 7:
    print('выходной')
elif day_n < 1 or day_n > 7:
    print('нет такого дня недели')
else: print('Не выходной')
    
