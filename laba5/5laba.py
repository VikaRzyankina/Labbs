#Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу
#сравнительного вычисления данной функции рекурсивно и итерационно. Определить (смоделировать) границы применимости
#рекурсивного и итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной
#и графической форме в виде отчета по лабораторной работе.
#21.	F(0) = F(1) = 1, F(n) = F(n–1)!, при n > 1

def recursive_f(n):
    if n < 2:
        return 1
    else:
        return 2 * recursive_f(n-1) + recursive_f(n-3)

def iterative_f(n):
    if n < 2:
        return 1
    f0, f1, f2 = 1, 1, 3
    for i in range(3, n + 1):
        fn = 2 * f2 + f0
        f0, f1, f2 = f1, f2, fn
    return fn if n > 2 else f2