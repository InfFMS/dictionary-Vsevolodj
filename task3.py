# Напишите программу, которая получает на вход строку и подсчитывает, 
# сколько раз в ней встречается каждый символ (независимо от регистра).
# Результат нужно вывести без фигурных скобок
# Пример. 
# ввод:
# Абракадабра
# Вывод
# а-5 б-2 д-1 к-1 р-2
keys = str(input())
my_dict = dict()
symbols = []
for symbol in keys:
    symbols += symbol
for elem in symbols:
    my_dict[elem] = symbols.count(elem)
str = str(my_dict)
str = str.replace("'", "")
str = str.replace(",", "")
str = str.replace(": ", "-")
str=str[1:-1]#{...}
print(str)
