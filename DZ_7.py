'''Задание 1.
Пользователь вводит с клавиатуры два числа.
Нужно посчитать отдельно сумму четных, нечетных и чисел,
кратных 9 в указанном диапазоне, а также среднеарифметическое каждой группы.'''
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите первое число: '))
sum1 = 0
count1 = 0
sum2= 0
count2 = 0
sum9 = 0
count9 = 0
for i in range(num1, num2+1):
    if i%2==0:
        sum1=sum1+i
        count1=count1+1
        avg1=sum1/count1
    if i%2!=0:
        sum2=sum2+i
        count2=count2+1
        avg2=sum2/count2
    if i%9==0:
        sum9=sum9+i
        count9=count9+1
        avg9=sum9/count9
print('Сумма четных чисел: ', sum1)
print('Среднеарифметическое для четны чисел: ', avg1)
print('Сумма нечетных чисел: ', sum2)
print('Среднеарифметическое для четны чисел: ', avg2)
print('Сумма кратных девяти равна: ', sum9)
print('Среднеарифметическое для чисел кратных девяти: ', avg9)

'''Задание 2.
Пользователь вводит с клавиатуры длину линии и символ для заполнения линии. 
Нужно отобразить на экране вертикальную линию из введенного символа, указанной длины.
Например, если было введено 5 и символ %, тогда вывод на экран будет такой:
%
%
%
%
%
'''
# line=int(input('Введите длину линии: '))
# symbol=str(input('Ведите символ: '))
# for i in range(line):
#     print(symbol)

'''Задание 3.
Пользователь вводит с клавиатуры числа. 
Если число больше нуля нужно вывести надпись «Numberis positive»,  
если меньше нуля «Numberis negative», 
если равно нулю «Number is equal to zero». 
Когда пользователь вводит число 7 программа прекращает свою работу и выводит на экран «Good bye!»'''

# while True:
#     number = int(input('Введите число: '))
#     if number>0:
#         print('«Numberis positive»')
#     elif number<0:
#         print('«Numberis negative»')
#     elif number==0:
#         print('«Number is equal to zero»')
#     if number==7:
#         break

'''Задание 4.
Пользователь вводит с клавиатуры числа. 
Программа должна подсчитывать сумму, максимум и минимум, введенных чисел. 
Когда пользователь вводит число 7 программа прекращает свою работу и выводит на экран надпись «Good bye!»'''

# while True:
#     number = int(input('Введите число: '))
#     if number>0:
#         print('«Numberis positive»')
#     elif number<0:
#         print('«Numberis negative»')
#     elif number==0:
#         print('«Number is equal to zero»')
#     if number==7:
#         break