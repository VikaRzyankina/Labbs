#Натуральные числа, содержащие не более двух групп из 5 подряд идущих 0.
#Список используемых в числах цифр выводить отдельно прописью.

import re
def repl(n):
    f = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь',
         9: 'девять'}
    return f.get(n)  # замена из словаря

file= open('../Invisible/text.txt', 'r')
while True:
    buffer=file.readline()
    if not buffer:
        print('Файл пустой')
        break
    res=re.findall(r'\b(?!\d*0{5}\d*0{5}\d*0{5}\d*)\d+\b',buffer)
if len(res) == 0:
    print('В файле нет подходящих под условие чисел')
    quit()
for j in res: #замена чисел прописью
    exp = []
    for i in j:
        if repl(int(i)) not in exp:
            exp.append(repl(int(i)))
    print(j + ' - ', *exp)
