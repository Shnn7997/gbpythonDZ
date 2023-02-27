# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input()
words = text.split()
res = []
for word in words:
    if 'абв' not in word:
        res.append(word)

print(' '.join(res))