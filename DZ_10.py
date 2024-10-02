'''Задание 1:
Пользователь вводит с клавиатуры арифметическое выражение. Например, 23+12.
Необходимо вывести на экран результат выражения.
В нашем примере это 35. Арифметическое выражение может состоять только из трёх частей: число, операция, число.
Возможные операции: +,-,*,/'''
math=input('Введите арифметическое выражение: ')

if '+' in math:
    num=math.split('+')
    print(math, '=', int(num[0])+int(num[1]))
if '-' in math:
    num = math.split('-')
    print(math, '=', int(num[0]) - int(num[1]))
if '*' in math:
    num = math.split('*')
    print(math, '=', int(num[0]) * int(num[1]))
if '/' in math:
    num = math.split('/')
    print(math, '=', int(num[0]) / int(num[1]))

'''Задание 2:
В списке целых, заполненном случайными числами, определить минимальный и максимальный элементы,
посчитать количество отрицательных элементов, посчитать количество положительных элементов, посчитать
количество нулей. Результаты вывести на экран.'''
numbers = input('Введите список целых чисел через пробел: ')
new_number=numbers.split()
array = list(map(int, new_number))
num_min=min(array)
num_max=max(array)
count_zero=0
count_positive=0
count_negative=0
for i in array:
    if i < 0:
        count_negative += 1
    if i > 0:
        count_positive+=1
    if i == 0:
        count_zero+=1
print('Максимальный элемент: ', num_max,
      '\nМинимальный элемент: ', num_min,
      '\nКоличество отрицательных элементов: ', count_negative,
      '\nКоличество положительных элементов: ', count_positive,
      '\nКоличество нулей: ', count_zero)
