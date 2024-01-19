file = input('Введите название файла с расширением:')
filename = file
count = 0
summ = 0
while filename.find('.txt') == -1:
    filename = input('Вы не ввели расширение .txt. Введите название файла с расширением:')
    with open(filename, 'r') as f:
        buffer = f.read().split(' ')
        print(buffer)
        for i in range(len(buffer)):
            print(buffer[i], i)
            if str(buffer)[i] % 2 == 0 and len(str(buffer)) == 5 and str(buffer)[0] == '7':
                count += 1
                summ += buffer[i]
            else:
                continue
            print(count, summ)
