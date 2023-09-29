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
        self.matrix = Matrix(
            accept_number('Введите количество строк массива: '),
            accept_number('Введите количество столбцов массива: ')
        )
        while True:
            handler_name = input('Выберите желаемый тип перебора массива (рекурсия - 0, итерация - 1): ')
            if handler_name == '0':
                print('Выбран рекурсивный обработчик.')
                self.handler = RecursiveHandler()
                break
            elif handler_name == '1':
                print('Выбран итеративный обработчик.')
                self.handler = IterativeHandler()
                break
            else:
                print('Введён неправильный тип обработчика.')

    def start(self):
        while True:
            self.process_matrix()
            next = input('Выбери следующее действие (перегенерация матрицы - 0, новая матрица - 1, выход - 2): ')
            if next == '0':
                self.matrix.regenerate()
                continue
            elif next == '1':
                self.matrix = Matrix(
                    accept_number('Введите количество строк массива: '),
                    accept_number('Введите количество столбцов массива: ')
                )
                continue
            elif next == '2':
                print('Выход из программы...')
                break
            else:
                print('Введено неизвестное действие.')

    def process_matrix(self):
        print('Начальный массив:')
        self.matrix.print()
        count = self.matrix.process(self.handler)
        print('Общее количество вариантов:', count)
        if count == 0:
            print('Проверяемый массив не подошел под условия.')
        else:
            print('Проверяемый массив подошел под условия.')

class Matrix:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.regenerate()

    def regenerate(self):
        self.array = [[random.randint(-10, 11) for i in range(self.height)] for j in range(self.width)]
        self.sums = [0] * self.height
        for i in range(self.height):
            if i % 2 == 1:
                for j in range(self.width):
                    self.sums[i] += self.array[j][i]
        return self.array

    def process(self, handler):
        return handler.handle(copy.deepcopy(self.array), self.sums) - 1

    def print(self):
        print_array(self.array)

class Handler:
    def handle(self, array, sums):
        return 0

class IterativeHandler(Handler):
    def handle(self, array, sums):
        print('Итеративный перебор возможных вариантов.')
        count = 0
        stack = [(array, 0, 0)]
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

            if array[row][column] > 0 and column % 2 == 1 and array[row][column] % 3 != 0 and sums[column] > 0:
                new_array = copy.deepcopy(array)
                new_array[row][column] = -new_array[row][column]
                stack.append((new_array, row, column + 1))
        return count


class RecursiveHandler(Handler):
    def handle(self, array, sums):
        print('Рекурсивный перебор возможных вариантов.')
        count = [0]
        self._handle(array, 0, 0, count, sums)
        return count[0]

    def _handle(self, array, row, column, count, sums):
        if column == len(array[row]):
            column = 0
            row += 1
        if row == len(array):
            print_array(array)
            count[0] += 1
            return
        self._handle(copy.deepcopy(array), row, column + 1, count, sums)

        if array[row][column] > 0 and column % 2 == 1 and array[row][column] % 3 != 0 and sums[column] > 0:
            new_array = copy.deepcopy(array)
            new_array[row][column] = -new_array[row][column]
            self._handle(new_array, row, column + 1, count, sums)


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


Program().start()
