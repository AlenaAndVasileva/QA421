'''Задание 1
Пользователь вводит с клавиатуры два числа.
Нужно посчитать сумму чисел в указанном диапазоне, а также среднеарифметическое.'''
# x = int(input("Введите число x: "))
# y = int(input("Введите число y: "))
# summa = 0
# count = 0
# for i in range(x, y + 1):
#     summa = summa + i
#     count= count+1
# print("Сумма чисел: ", summa)
# print("Среднеарифметическое: ",summa/count)

'''Задание 2
Пользователь вводит с клавиатуры число. 
Требуется посчитать факториал числа. Например, если введено 3, факториал числа 1*2*3 = 6.
Формула для расчета факториала: n! = 1*2*3…*n,где n — число для расчета факториала.'''
# x = int(input("Введите число x: "))
# f=x
# for i in range(1,x):
#     f=f*i
# print("Факториал числа: ", f)

'''Задание 3
Пользователь вводит с клавиатуры длину линии.
Нужно отобразить на экране горизонтальную линию из *, указанной длины.
Например, если было введено 7, тогда вывод на экран будет такой: *******.'''
# line=int(input('Введите длину линии: '))
# for i in range(line):
#     print("*", end="")

'''Задание 4
Пользователь вводит с клавиатуры длину линии и символ для заполнения линии. 
Нужно отобразить на экране горизонтальную линию из введенного символа, указанной длины.
Например, если было введено 5 и &, тогда вывод на экран будет такой: &&&&&.'''
line=int(input('Введите длину линии: '))
symbol=str(input('Ведите символ: '))
for i in range(line):
    print(symbol, end="")