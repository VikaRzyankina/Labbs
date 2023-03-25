# С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E
# заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное заполнение, а целенаправленное.

# 21.	Формируется матрица F следующим образом: если в В количество нулей в нечетных столбцах в области 3 больше,
# чем сумма чисел в четных строках в области 1, то поменять в С симметрично области 2 и 3 местами,
# иначе В и Е поменять местами несимметрично. При этом матрица А не меняется.
# После чего вычисляется выражение: A*F-K*F T . Выводятся по мере формирования А, F и все матричные операции последовательно.
#                       1
#  E   B            4      2
#  D   C                3

import random
def print_matrix(matrix):     #вывод матрицы
  for row in matrix:
    for elem in row:
      print('{:4}'.format(elem), end=' ')
    print()

def paste_matrix(matrix_F, matrix, column_index, row_index):
  uwu = column_index
  for row in matrix:
    for element in row:
      matrix_F[row_index][column_index] = element
      column_index += 1
    row_index += 1
    column_index = uwu

def matrix_zero(size):
        return [[0 for i in range(size)] for j in range(size)]

def matrix_input(matrix,i1,i2,j1,j2):
    zero_matrix=matrix_zero(len(matrix)//2)
    for i in range(i1, i2):
        for j in range(j1,j2):
            zero_matrix[i-(i1)][j-(j1)] = matrix[i][j]
    return zero_matrix

try:

    K = int(input("Введите число K, являющееся коэффициентом при умножении: \n "))
    n = int(input("Введите число число N, больше 5, являющееся порядком квадратной матрицы:\n "))
    while n < 5 :        # ошибка в случае введения неодходящего порядка матрицы
        n = int(input("Вы ввели число, неподходящее по условию - введите число N, большее или равное 5:\n"))
except ValueError:  # ошибка на случай введения не числа в качестве порядка или коэффициента
    print("Введенный символ не является числом. Перезапустите программу и введите число")
    exit(0)

print("Матрица А изначальная:")
#matrix_A = [[random.randint(-10, 10) for i in range(n)] for j in range(n)]    # создаем матрицу размером nxn, заполненную случайными числами
#matrix_A = [[i+j*n for i in range(n)] for j in range(n)]        # или задание матрицы для тестирования
matrix_A = [[(1) for i in range(n)] for j in range(n)]          # или задание единичной матрицы для тестирования
print_matrix(matrix_A)          # вывод матрицы A

print('E   B       1')
print('D   C    4     2')
print('            3')

half_n = n//2
fix_n=half_n
if n % 2 != 0:
    fix_n+=1


matrix_C=matrix_input(matrix_A,fix_n,n,fix_n,n)  # подматрица C матрицы A

matrix_B = matrix_input(matrix_A,0,half_n,fix_n,n)  # подматрица В матрицы A
print('Подматрица B матрицы A:')
print_matrix(matrix_B)

matrix_E = matrix_input(matrix_A,0,half_n,0,half_n)    # подматрица E матрицы A

matrix_D = matrix_input(matrix_A,fix_n,n,0,half_n) #  подматрица D матрицы A
zero, summ = 0,0        # счетчик нулей в области 3, сумма чисео в области 1

for i in range ((n // 4) +1):         #область 1
    for j in range (i, half_n - i):
        if (i+1) % 2 ==0:
            summ+=matrix_B[i][j]
print('Сумма чисел в четных строках в области 1:',summ)

for i in range (n // 4, half_n ):      #область 3
    for j in range (half_n-i-1,i+1):
        if (j + 1) % 2 != 0 and matrix_B[i][j]==0:
            zero+=1
print('Количество нулей в нечетных столбцах в области 3:',zero)
if summ < zero:
    print('Количество нулей в области 3 больше суммы чисел в области 1 - меняем симметрично в подматрице С области 2 и 3 местами')
    print('Начальная подматрциа C:')
    print_matrix(matrix_C)
    for i in range(n // 4, half_n):
        for j in range(half_n - i - 1, i + 1):
            matrix_C[i][j], matrix_C[j][i] = matrix_C[j][i], matrix_C[i][j]
    print('Получившаяся подматрица С:')
    print_matrix(matrix_C)
else:
    print('Количество нулей в области 3 оказалось меньше суммы чисел в области 1 - меняем местами подматрицы E и B')
    matrix_E, matrix_B = matrix_B, matrix_E

matrix_F=matrix_A.copy()
paste_matrix(matrix_F, matrix_E, 0, 0)
paste_matrix(matrix_F, matrix_B, fix_n, 0)
paste_matrix(matrix_F, matrix_C, fix_n, fix_n)
paste_matrix(matrix_F, matrix_D, 0, fix_n)

print('Созданная по условию матрица F:')
print_matrix(matrix_F)

matrix_F_transp = matrix_zero(n)  # пустая транспонированая матрица

print("Матрица F транспонированая:")
for i in range(n):
    for j in range(n):
        matrix_F_transp[i][j] = matrix_F[j][i]
print_matrix(matrix_F_transp)

print('Вычисляем выражение  A*F-K*FT:')

matrix_AF = matrix_zero(n)  # заготовка под умножение матриццы A на матрицу F
matrix_KF = matrix_F_transp.copy()  # копируем транспонированую матрицу F
for i in range(n):
    for j in range(n):
        for k in range(n):
            matrix_AF[i][j]+=matrix_A[i][k]*matrix_F[k][j]
print('Результат умножения матриц A и F:')
print_matrix(matrix_AF)

for i in range(n):
    for j in range(n):
        matrix_KF[i][j]*= K
print('Результат умножения коэффициента K на матрицу F транспонированую:')
print_matrix(matrix_KF)
matrix_res = matrix_zero(n)   #заготовка под результат вычислений
for i in range(n):
    for j in range(n):
        matrix_res[i][j]=matrix_AF[i][j] - matrix_KF[i][j]
print(''
      'Конечный результат всех вычислений')
print_matrix(matrix_res)
