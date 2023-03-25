#Натуральные числа, содержащие не более двух групп из 5 подряд идущих 0.
#Список используемых в числах цифр выводить отдельно прописью.
def repl(n):
    f = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь',
         9: 'девять'}
    return f.get(n)  # замена из словаря
uwu=[]
buffer_len=1
work_buffer=''
work_buffer_len=buffer_len
with open('../Invisible/text.txt', 'r') as f:
    buffer=f.read(buffer_len)
    if not buffer:
        print('Файл пустой')
    while buffer:
        while buffer >='0' and buffer <='9':
            work_buffer+=buffer
            buffer=f.read(buffer_len)
        if work_buffer:
            kn = 0
            pn = 0
            for j in work_buffer:
                    if j == '0':
                        kn += 1
                        if kn == 5:
                            pn += 1
                            kn = 0
                    elif j != '0':
                        kn = 0
            if pn<3:
                uwu.append(work_buffer)
        work_buffer=''
        buffer=f.read(buffer_len)
if len(uwu) == 0:
    print('В файле нет подходящих под условие чисел')
    quit()
for j in uwu: #замена чисел прописью
    exp = []
    for i in j:
        if repl(int(i)) not in exp:
            exp.append(repl(int(i)))
    print(j + ' - ', *exp)