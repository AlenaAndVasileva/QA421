'''Задание 1.
Пользователь вводит с клавиатуры номер дня недели (1-7).
Необходимо вывести на экран названия дня недели.
Например, если 1, то на экране надпись понедельник, 2- вторинк и т.д.'''

# day = int(input('Введите номер дня недели от 1 до 7: '))
# if day == 1:
#     print('Понедельник')
# elif day == 2:
#     print('Вторник')
# elif day == 3:
#     print('Среда')
# elif day == 4:
#     print('Четверг')
# elif day == 5:
#     print('Пятница')
# elif day == 6:
#     print('Суббота')
# elif day == 7:
#     print('Воскресенье')
# else:
#     print('В недели только 7 дней. Введите от 1 до 7.')

'''Задание 2.
Пользователь вводит с клавиатуры номер месяца (1-12). 
Необходимо вывести на экран название месяца.
Например, если 1, то на экране надпись январь, 2 — февраль и т.д.'''

# mounth = int(input('Введите номер месяца от 1 до 12: '))
# if mounth == 1:
#     print('Январь')
# elif mounth == 2:
#     print('Февраль')
# elif mounth == 3:
#     print('Март')
# elif mounth == 4:
#     print('Апрель')
# elif mounth == 5:
#     print('Май')
# elif mounth == 6:
#     print('Июнь')
# elif mounth == 7:
#     print('Июль')
# elif mounth == 8:
#     print('Август')
# elif mounth == 9:
#     print('Сентябрь')
# elif mounth == 10:
#     print('Октябрь')
# elif mounth == 11:
#     print('Ноябрь')
# elif mounth == 12:
#     print('Декабрь')
# else:
#     print('В году только 12 месцев. Введите от 1 до 12.')

'''Задание 3.
Пользователь вводит с клавиатуры число. 
Если число больше нуля нужно вывести надпись «Numberis positive»,
если меньше нуля «Number is negative», 
если равно нулю «Number is equal to zero»'''

# number = int(input('Введите число:\n'))
# if number > 0:
#     print('«Numberis positive»')
# elif number < 0:
#     print('«Number is negative»')
# else:
#     print('«Number is equal to zero»')

'''Задание 4
Пользователь вводит два числа. Определить, равны ли эти числа, и, если нет, вывести их на экран в порядке возрастания.'''

number1 = int(input('Введите первое число: \n'))
number2 = int(input('Введите второе число: \n'))
if number1 < number2:
    print('Числа не равны: ', number1, number2)
elif number1 > number2:
    print('Числа не равны: ', number2, number1)
else:
    print('Числа равны')