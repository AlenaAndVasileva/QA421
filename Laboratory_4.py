'''Задание 1
Пользователь вводит с клавиатуры два числа.
Нужно показать все числа в указанном диапазоне.'''
# number1 = int(input('Введите первое число: '))
# number2 = int(input('Введите второе число: '))
# for i in range (number1, number2+1):
#     print(i)

'''Задание 2
Пользователь вводит с клавиатуры два числа. 
Нужно показать все нечетные числа в указанном диапазоне.'''
# number1 = int(input('Введите первое число: '))
# number2 = int(input('Введите второе число: '))
# for i in range (number1, number2+1):
#     if i%2==1:
#         print(i, end = ' ')

# '''Задание 3
# Пользователь вводит с клавиатуры два числа.
# Нужно показать все четные числа в указанном диапазоне.'''
# number1 = int(input('Введите первое число: '))
# number2 = int(input('Введите второе число: '))
# for i in range (number1, number2+1):
#     if i%2==0:
#         print(i, end = ' ')

'''Задание 4
Пользователь вводит с клавиатуры два числа. 
Нужно показать все числа в указанном диапазоне в порядке убывания.'''
# number1 = int(input('Введите первое число: '))
# number2 = int(input('Введите второе число: '))
# for i in range (number2, number1-1, -1):
#     print(i)

'''Задание 5
Пользователь вводит с клавиатуры два числа. 
Нужно показать все нечетные числа в указанном диапазоне.
Если границы диапазона указаны неправильно требуется произвести нормализацию границ. 
Например, пользователь ввел 33 и 13, требуется нормализация после которой начало диапазона станет равно 13, а конец 33.'''
number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
if number1<number2:
    for i in range(number1, number2 + 1):
            if i % 2 == 1:
                print(i, end=' ')
elif number1>number2:
        for i in range(number2, number1+1):
            if i % 2 == 1:
                print(i, end=' ')