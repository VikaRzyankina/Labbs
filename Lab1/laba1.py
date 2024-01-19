count = 0
summ = 0
while True:
    file = input('Введите название файла с расширением:')
    filename = file
    try:
        with open(filename, 'r') as f:
            buffer = f.read().split(' ')
            for i in buffer:
                if int(i) % 2 == 0 and len(str(i)) == 5 and str(i)[0] == '7':
                    count += 1
                    summ += int(i)
                else:
                    continue
        print('Количество:',count,',Cумма:', summ)
        break
    except FileNotFoundError:
        continue
