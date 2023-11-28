# Вычислить сумму знакопеременного ряда |х*n|/n!, где х-матрица ранга к (к и матрица задаются случайным образом), n - номер слагаемого.
# Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой. У алгоритма д.б. линейная сложность.
# Знак первого слагаемого  -.

import random
import numpy as np
from decimal import Decimal, getcontext


def s_sum(x, t):
    n = 1  # Номер слагаемого
    curr_x = x  # Текущая матрица
    factorial = 1  # Накопляемый факториал
    res = 0  # Переменная результата
    sign = -1  # Переменная для смены знака

    while True:
        curr_term = Decimal(np.linalg.det(curr_x) * n) / Decimal(factorial)  # Вычисляем текущий член ряда
        res += sign * curr_term  # Прибавляем его к результату с учетом знака

        # Проверка на достижение точности
        if abs(curr_term) < 1 / Decimal(10 ** t):
            break
        n += 1
        sign *= -sign
        factorial *= n
        curr_x *= x

    return res

print("Введите число t, являющееся количеством знаков после запятой (точностью):")
t = int(input())
while t < 1:
    t = int(input("Вы ввели число, неподходящее по условию, введите число t, большее или равное 1:\n"))

print()

# Генерация случайного значения k и матрицы x
def matrix():
    k = random.randint(1, 10)
    x = np.random.randint(-1, 1, (k, k))
    if abs(np.linalg.det(x)) == 0:
        return matrix()
    else:
        return x

x = matrix()

# Вывод матрицы x
print("Сгенерированная матрица:")
print(x)
print()

# Установка технической точности вычислений
getcontext().prec = t
result = s_sum(x, t)
print(f"Сумма ряда с точностью {t} знаков после запятой: {result:.{t}f}".rstrip('0').rstrip('.'))
