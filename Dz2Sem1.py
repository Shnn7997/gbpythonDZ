
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

flag = True
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            func = not(x or y or z) == (not x and not y and not z)
            if func == False:
                flag = False
if flag:
    print('Доказано')
else:
    print('Не всегда')