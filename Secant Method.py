# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def secant_method(f,x0,x1,e,N):
    print('\n\n***Работа Метода Секущих***')
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Разница значений функции равно нулю!')
            break

        x2 = x0 - (x1-x0)*f(x0)/(f(x1) - f(x0))
        print('Шаг-%d, x2 = %0.4f and f(x2) = %0.4f' % (step, x2, f(x2)))
        x0 = x1
        x1 = x2
        step = step + 1

        if step > N:
            print('Точки не сошлись за %d итераций' % (N))
            break

        condition =(abs(f(x2)) > e)
    print('\n Корень уравнения = %0.8f' % x2)


# Input Section
x0 = input('Введите левую границу: ')
x1 = input('Введите правую границу: ')
e = input('Введите пограшность "e": ')
N = input('Количество итераций: ')

# Конвертируем x0, x1 и e во float
x0 = float(x0)
x1 = float(x1)
e = float(e)

# Конвертируем N в int
N = int(N)

# Метод секущей
secant_method(lambda x: x**3-x+1,x0,x1,e,N)