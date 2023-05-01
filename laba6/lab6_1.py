'''

Вариант 21. Дан двумерный массив. Сформировать все возможные варианты данного массива путем
замены положительных элементов в четных столбцах на отрицательные элементы, равные по модули.
1 часть – написать программу в соответствии со своим вариантом задания.

'''

import random
import copy

def accept_number(description):
    while True:
        try:
            k = int(input(description))
            if k > 0:
                return k
            else:
                print('Введенное число отрицательное.')

        except ValueError:
            print('Введенное значение не является числом.')

def print_array(array):                # Вывод массива
    for row in array:
        for elem in row:
            print('{:4}'.format(elem), end=' ')
        print()
    print()

def F_rec(array, row, column, count):           # Рекурсивное решение задачи
    if column == len(array[row]):
        column = 0
        row += 1
    if row == len(array):
        print_array(array)
        count[0] += 1
        return
    F_rec(copy.deepcopy(array), row, column + 1, count)

    if array[row][column] > 0 and column % 2 == 1:
        new_array=copy.deepcopy(array)
        new_array[row][column] = -new_array[row][column]
        F_rec(new_array, row, column + 1, count)

def F_iter(array):                          # Итеративное решение задчи
    count = 0
    stack = [(copy.deepcopy(array), 0, 0)]
    while stack:  # пока не пусто
        array, row, column = stack.pop()
        if column == len(array[row]):
            column = 0
            row += 1
        if row == len(array):
            count += 1
            print_array(array)
            continue
        stack.append((copy.deepcopy(array), row, column + 1))

        if array[row][column] > 0 and column % 2 == 1:
            new_array = copy.deepcopy(array)
            new_array[row][column] = -new_array[row][column]
            stack.append((new_array, row, column + 1))
    print('Общее количество вариантов: ', count - 1)

count = [0]
n=accept_number('Введите ширину массива: ')
m=accept_number('Введите высоту массива: ')
array = [[random.randint(-10, 10) for i in range(n)] for j in range(m)]

print('Рекурсивный перебор возможных вариантов.')
F_rec(array, 0, 0, count)
print('Общее количество вариантов: ', count[0] - 1)

print('Итеративный перебор возможных вариантов.')
F_iter(array)

cr=count[0]-1
if cr == 0:
    print('Проверяемый массив не подошел под условия.')

