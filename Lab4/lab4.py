#21.	Формируется матрица F следующим образом: скопировать в нее А и  если в В количество нулей в нечетных столбцах,больше
# чем сумма чисел в четных строках , то поменять местами  В и С симметрично, иначе В и Е поменять местами несимметрично.
# При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F,то
# вычисляется выражение:A^(-1)*AT – K * FТ, иначе вычисляется выражение (AТ +G-F^(-1)*K, где G-нижняя треугольная матрица, полученная из А.
# Выводятся по мере формирования А, F и все матричные операции последовательно.

#  E   B
#  D   C
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

k = int(input("Введите число K являющееся коэффициентом при умножении: "))
n = int(input("Введите число n больше 3 которое являеться рзмером матрицы: "))
while n <= 3:
        n = int(input("\nВведите число больше 3 "))
A = np.random.randint(-10.0, 11.0, (n, n))
#A = np.ones((n,n))      # или задание единичной матрицы для тестирования
print("\nМатрица A:\n", A)

half_n = n//2
maxfix_n=half_n
minfix_n=half_n
if n % 2 != 0:
    maxfix_n+=1
    minfix_n= maxfix_n - 1
    
F = A.copy()
E = np.array(A[:minfix_n, :minfix_n ])
B = np.array(A[:minfix_n, maxfix_n:])
print('\n Подматрица B матрицы A:\n',B)
C = np.array(A[maxfix_n:, maxfix_n:])
D= np.array(A[maxfix_n:, :minfix_n])

zeros_B=np.sum(np.count_nonzero(B[:,0::2]==0))
sum_B=np.sum(B[1::2,:])

if sum_B < zeros_B:
        print("\nМеняем симметрично B и C")
        F[:minfix_n,maxfix_n:] = C [-1::-1, :minfix_n]
        F[maxfix_n:, maxfix_n:] = B [-1::-1,:minfix_n]
else:
    print("\nМеняем несимметрично B и Е")
    F[:minfix_n, maxfix_n:] = E
    F[:minfix_n, :minfix_n] = B
print(F)
trans_A=np.transpose(A)
det_A=np.linalg.det(A)
diag_F=np.trace(F)
if det_A> diag_F:

    print('\n Вычисляем выражение : A^-1 * AT – K * FТ ')
    power_A = np.linalg.matrix_power(A, -1)
    print('\nВозведение матрицы А в -1 степень:\n', power_A)
    print('\nТранспонированая матрица A:\n', trans_A)
    mod_A=np.dot(power_A, trans_A)
    print('\nУмножение A^-1 * AT\n', mod_A)
    trans_F=np.transpose(F)
    print('\nТранспоинрованая матрица F:\n',trans_F)
    mod_trans_F = np.dot(k, trans_F)
    print('\nУмножение K *FT\n',mod_trans_F)
    print('\nРазница матриц')
    result=np.subtract(mod_A, mod_trans_F)

else:
    print('\n Вычисляем выражение:(AТ + G - F^-1) * K ')
    print('\nТранспонированая матрица А:\n', trans_A)
    G=np.tril(A)
    print('\nНижняя треугольная матрица G из матрицы A:\n',G)
    ATG = np.add(trans_A, G)
    print('\nСумма AT + G:\n',ATG)
    power_F = np.linalg.matrix_power(F, -1)
    print('\nВозведение матрицы F в -1 степень:\n',power_F)
    sub_ATGF = np.subtract(ATG, power_F)
    print('\nРазница между AT + G - F^-1:\n',sub_ATGF)
    result=np.dot(sub_ATGF, k)
    print('\nУмножение на K\n',result)
print ('\nРезультат вычислений\n', result)

explode = [0] * (n - 1)
explode.append(0.1)
plt.title("Круговая диаграмма")
try:
    sizes = [round(np.mean(abs(F[i, ::])) * 100, 1) for i in range(n)]
except IndexError:
    sizes = [round(np.mean(abs(F[i, ::])) * 100, 1) for i in range(n)]
plt.pie(sizes, labels=list(range(1, n + 1)), explode=explode, autopct='%1.1f%%', shadow=True)
plt.show()

plt.plot(A)
plt.title("График")
plt.ylabel("y axis")
plt.xlabel("x axis")
plt.show()

sns.heatmap(A, cmap="Spectral", annot = True)
plt.title("Тепловая карта")
plt.ylabel("Номер строки")
plt.xlabel("Номер столбца")
plt.show()


