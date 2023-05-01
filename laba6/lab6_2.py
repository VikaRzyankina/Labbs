'''

Вариант 21. Дан двумерный массив. Сформировать все возможные варианты данного массива путем
замены положительных элементов в четных столбцах на отрицательные элементы, равные по модули.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно
ограничение на характеристики объектов и целевую функцию для оптимизации решения.
+ Проверяемый элемент массива не должен быть кратен 3.
+ Сумма элементов столбца изначального массива проверяемого элемента должна быть не отрицательной.

'''

import random
import copy

def accept_number(description):           # Проверка символа на цифру
    while True:
        try:
            k = int(input(description))
            if k > 0:
                return k
            else:
                print('Введенное число отрицательное.')

        except ValueError:
            print('Введенное значение не является числом.')

def print_array(array):                         # Вывод массива
    for row in array:
        for elem in row:
            print('{:4}'.format(elem), end=' ')
        print()
    print()

def F_rec(array, row, column, count, summ):    # Рекурсивное решение задачи
    if column == len(array[row]):
        column = 0
        row += 1
    if row == len(array):
        print_array(array)
        count[0] += 1
        return
    F_rec(copy.deepcopy(array), row, column + 1, count, summ)

    if array[row][column] > 0 and column % 2 == 1 and array[row][column] % 3 != 0 and summ[column] > 0:
        new_array=copy.deepcopy(array)
        new_array[row][column] = -new_array[row][column]
        F_rec(new_array, row, column + 1, count, summ)


def F_iter(array):                          # Итеративное решение задачи
    count = 0
    stack = [(copy.deepcopy(array), 0, 0)]
    while stack:                            # пока не пусто
        array, row, column = stack.pop()
        if column == len(array[row]):
            column = 0
            row += 1
        if row == len(array):
            count += 1
            print_array(array)
            continue
        stack.append((copy.deepcopy(array), row, column + 1))

        if array[row][column] > 0 and column % 2 == 1 and array[row][column] % 3 != 0 and summ[column] > 0:
            new_array = copy.deepcopy(array)
            new_array[row][column] = -new_array[row][column]
            stack.append((new_array, row, column + 1))
    print('Общее количество вариантов: ', count - 1)

count = [0]
n=accept_number('Введите ширину массива: ')
m=accept_number('Введите высоту массива: ')

array = [[random.randint(-10, 11) for i in range(n)] for j in range(m)]

summ = [0] * n
print_array('Начальный массив', array)
for i in range(n):
    for j in range(m):
        if i % 2 == 1:
            summ[i] += array[j][i]

print('Рекурсивный перебор возможных вариантов.')
F_rec(array, 0, 0, count, summ)
print('Общее количество вариантов: ', count[0] - 1)
print('Итеративный перебор возможных вариантов.')
F_iter(array)
cr=count[0]-1
if cr == 0:
    print('Проверяемый массив не подошел под условия.')


