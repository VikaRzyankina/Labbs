'''

Вариант 21. Дан двумерный массив. Сформировать все возможные варианты данного массива путем
замены положительных элементов в четных столбцах на отрицательные элементы, равные по модули.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно
ограничение на характеристики объектов и целевую функцию для оптимизации решения.
+ Проверяемый элемент массива не должен нацело делиться на 3.
+ Сумма элементов столбца изначального массива проверяемого элемента должна быть не отрицательной.

'''

import random
import copy


class Program:
    def __init__(self):
        self.row = accept_number('Введите ширину массива: ')
        self.column = accept_number('Введите высоту массива: ')
        while (True):
            handler_name = input('Выберите желаемый тип перебора массива (rec, iter): ')
            if handler_name == 'rec':
                self.handler = RecursiveHandler()
                break
            elif handler_name == 'iter':
                self.handler = IterativeHandler()
                break
            else:
                print('Введено неправильное имя обработчика.')

    def start(self):
        array = [[random.randint(-10, 11) for i in range(self.row)] for j in range(self.column)]
        summ = [0] * self.row
        print('Начальный массив:')
        print_array(array)
        for i in range(self.row):
            for j in range(self.column):
                if i % 2 == 1:
                    summ[i] += array[j][i]
        count = self.handler.process(array, summ) - 1
        print('Общее количество вариантов: ', count)
        if count == 0:
            print('Проверяемый массив не подошел под условия.')


class Handler:
    def process(self, array, summ):
        return 0


class IterativeHandler(Handler):
    def process(self, array, summ):
        print('Итеративный перебор возможных вариантов.')
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

            if array[row][column] > 0 and column % 2 == 1 and array[row][column] % 3 != 0 and summ[column] > 0:
                new_array = copy.deepcopy(array)
                new_array[row][column] = -new_array[row][column]
                stack.append((new_array, row, column + 1))
        return count


class RecursiveHandler(Handler):
    def process(self, array, summ):
        print('Рекурсивный перебор возможных вариантов.')
        count = [0]
        self._process(array, 0, 0, count, summ)
        return count[0]

    def _process(self, array, row, column, count, summ):
        if column == len(array[row]):
            column = 0
            row += 1
        if row == len(array):
            print_array(array)
            count[0] += 1
            return
        self._process(copy.deepcopy(array), row, column + 1, count, summ)

        if array[row][column] > 0 and column % 2 == 1 and array[row][column] % 3 != 0 and summ[column] > 0:
            new_array = copy.deepcopy(array)
            new_array[row][column] = -new_array[row][column]
            self._process(new_array, row, column + 1, count, summ)


def accept_number(description):  # Проверка символа на цифру
    while True:
        try:
            k = int(input(description))
            if k > 0:
                return k
            else:
                print('Введенное число отрицательное.')

        except ValueError:
            print('Введенное значение не является числом.')


def print_array(array):  # Вывод массива
    for row in array:
        for elem in row:
            print('{:4}'.format(elem), end=' ')
        print()
    print()


program = Program()
program.start()
