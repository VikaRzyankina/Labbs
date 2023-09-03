'''

Вариант 21. Дан двумерный массив. Сформировать все возможные варианты данного массива путем
замены положительных элементов в четных столбцах на отрицательные элементы, равные по модули.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно
ограничение на характеристики объектов и целевую функцию для оптимизации решения.
+ Проверяемый элемент массива не должен нацело делиться на 3.
+ Сумма элементов столбца изначального массива проверяемого элемента должна быть не отрицательной.

'''

import tkinter as tk
import random
import copy


class Program:
    def __init__(self,main):
        self.main = main
        tk.Label(main, text="Дан двумерный массив. Сформировать все возможные варианты данного массива путем"
                                   "\nзамены положительных элементов в четных столбцах на отрицательные элементы, равные по модули."
                                   "\nПроверяемый элемент массива не должен нацело делиться на 3."
                                   "\nСумма элементов столбца изначального массива проверяемого элемента должна быть не отрицательной.").pack()


        tk.Label(main, text="Введите ширину массива: ").pack()
        self.entry1 = tk.Entry(main, width=30, justify='center')
        self.entry1.pack()

        tk.Label(main, text="Введите высоту массива: ").pack()
        self.entry2 = tk.Entry(main, width=30, justify='center')
        self.entry2.pack()

        tk.Label(main,text="Выберите желаемый тип перебора массива (rec, iter): ").pack()
        self.entry3 = tk.Entry(main,width=30, justify='center')
        self.entry3.pack()

        self.button_main = tk.Button(main,text="Начать", command=self.check_input)
        self.button_main.pack()

        self.button_exit = tk.Button(main, text="Выход", command=window.destroy)
        self.button_exit.pack(anchor="se")
        self.main.mainloop()

    def check_input(self):
        self.row = accept_number(self.entry1.get())
        self.column = accept_number(self.entry2.get())
        if self.row is None or self.column is None:
            return
        handler_name = self.entry3.get()
        if handler_name == 'rec':
            self.handler = RecursiveHandler()
        elif handler_name == 'iter':
            self.handler = IterativeHandler()
        else:
            text_window('Введенное неправильное имя обработчика.')
            return
        self.start()

    def start(self):
        array = [[random.randint(-10, 11) for i in range(self.row)] for j in range(self.column)]
        summ = [0] * self.row
        root = tk.Tk()
        tk.Label(root, text='Начальный массив:').pack()
        tk.Label(root, text=array_string(array)).pack()
        for i in range(self.row):
            for j in range(self.column):
                if i % 2 == 1:
                    summ[i] += array[j][i]
        count = self.handler.process(array, summ, root) - 1
        root.title("Ответ")
        tk.Label(root,width=90, text=f'Общее количество вариантов: {count}').pack()
        if count == 0:
            tk.Label(root, width=90, text='Проверяемый массив не подошел под условия.').pack()
        self.button_exit = tk.Button(root, text="Выход", command=root.destroy)
        self.button_exit.pack(anchor="se")

class Handler:
    def process(self, array, summ, root):
        return 0


class IterativeHandler(Handler):
    def process(self, array, summ, root):
        tk.Label(root, width=90, text='Итеративный перебор возможных вариантов.').pack()
        count = 0
        stack = [(copy.deepcopy(array), 0, 0)]
        while stack:  # пока не пусто
            array, row, column = stack.pop()
            if column == len(array[row]):
                column = 0
                row += 1
            if row == len(array):
                count += 1
                tk.Label(root, width=90, text=array_string(array)).pack()
                continue
            stack.append((copy.deepcopy(array), row, column + 1))

            if array[row][column] > 0 and column % 2 == 1 and array[row][column] % 3 != 0 and summ[column] > 0:
                new_array = copy.deepcopy(array)
                new_array[row][column] = -new_array[row][column]
                stack.append((new_array, row, column + 1))
        return count


class RecursiveHandler(Handler):
    def process(self, array, summ, root):
        tk.Label(root, text='Рекурсивный перебор возможных вариантов.').pack()
        count = [0]
        self._process(array, 0, 0, count, summ, root)
        return count[0]

    def _process(self, array, row, column, count, summ, root):
        if column == len(array[row]):
            column = 0
            row += 1
        if row == len(array):
            tk.Label(root, width=90, text=array_string(array)).pack()
            count[0] += 1
            return
        self._process(copy.deepcopy(array), row, column + 1, count, summ, root)

        if array[row][column] > 0 and column % 2 == 1 and array[row][column] % 3 != 0 and summ[column] > 0:
            new_array = copy.deepcopy(array)
            new_array[row][column] = -new_array[row][column]
            self._process(new_array, row, column + 1, count, summ, root)

def text_window(message):
  window = tk.Tk()
  window.title('Ошибка')
  tk.Label(window, text=message).pack()


def accept_number(value):  # Проверка символа на цифру
    try:
        k = int(value)
        if k > 0:
            return k
        else:
            text_window("Введенное число отрицательное.")
    except ValueError:
        text_window("Введенное значение не является числом.")

def array_string(array):
    array_str='' # Вывод массива
    for row in array:
        for elem in row:
            array_str += ('{:4} '.format(elem))
        array_str+='\n'
    return array_str


window = tk.Tk()
window.title('Перебор массива')

program = Program(window)
