#1) Создать переменную типа String
a = 'Alina'

#2) Создать переменную типа Integer
b = 37

#3) Создать переменную типа Float
fl_c = 36.6

#4) Создать переменную типа Bytes
b_type = bytes(123)

#5) Создать переменную типа List
list = ['alina','roma','misha', 123, True,['15','26']]

#6) Создать переменную типа Tuple
f = tuple('hello, world!')

#7) Создать переменную типа Set
j = set('hello')

#8. Создать переменную типа Frozen set
k = frozenset('qwerty')

#9) Создать переменную типа Dict
dict_type = {"key1":6,
             "name1":"roma"}

#10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(type(a),a)
print(type(b),b)
print(type(fl_c),fl_c)
print(type(list),list)
print(type(f),f)
print(type(j),j)
print(type(k),k)
print(type(dict_type),dict_type)

#11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
name = 'alina '
surname = 'makarava'
surname_name = name + surname
print('surname_name:', surname_name)

#12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)

Name = 'alina'
age = '37'
print(Name, age)

#13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)

name_first = 'alina'
age = 37
print(name + str(age))