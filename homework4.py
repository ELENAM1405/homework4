my_string=input('Кто_является_автором_данных_строк?,_"Что_за_диво!_Все_так_чисто_и_красиво._Кто-то_терем_прибирал_Да_хозяев_поджидал.": ')
print("Ваш ответ: ", (my_string))

my_string=('Сколько символов в тексте?: "Что_за_диво!_Всё_так_чисто_и_красиво"')
print(my_string)
my_string=('"Что_за_диво!_Все_так_чисто_и_красиво"')
print('Ответ: ',len(my_string))

my_string=input('Сколько символов в тексте?: ')
print('Ответ:',len(my_string))

print('Строка в верхнем регистре "Что_за_диво!_Все_так_чисто_и_красиво"'.upper())

my_string=input('Написать строку в верхнем регистре: ')
print((my_string).upper())

print('Строка в нижнем регистре "Что_за_диво!_Все_так_чисто_и_красиво"'.lower())

my_string=input('Написать строку в нижнем регистре: ')
print((my_string).lower())

print('Удалить все пробелы в строке: ', '"Что_за_диво!_Все_так_чисто_и_красиво"'.replace('_',''))

my_string=input('Удалить все пробелы в строке: ')
print((my_string).replace(' ',''))

my_string=input('Вывести первый символ строки: ')
print(my_string[0])

my_string=input('Вывести последний символ строки: ')
print(my_string[-1])

