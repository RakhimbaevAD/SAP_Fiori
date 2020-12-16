from math import factorial # Импортируем функцию для нахождения факториала из модуля math

N = input('Введите число: ')

N = str(factorial(int(N)))

print('Вычисленный факториал: {0}'.format(N))

index = -1
zero_counter = 0

if N[index] == '0':
    while(N[index] == '0'):
        zero_counter += 1
        index -= 1

print('Количество нулей на конце: {0}'.format(zero_counter))