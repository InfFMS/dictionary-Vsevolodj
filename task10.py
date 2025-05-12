# Нужно считать файл parameters.txt. 
# Это файл с настройками расчетной модели.
# Формат в файле следующий первое слово в строке - это ключ, 
# потом после пробела - значение (может быть строкой, числом, или набором чисел),
# все, что после символа "//" это комментарий  должно игнорироваться.
# Реализуйте считывание значений из файла и запись этих значений в словарь.
f = open('parameters.txt', 'r')
f =f.read()
text = f.split("\n")
mydict = {}
for i in range(0,len(text)):
    index = text[i].find("//")
    if index != -1:
        text[i]=text[i][0:index]
for i in range(0,len(text)):
    index2 = text[i].find(" ")
    mydict[text[i][0:index2]] = text[i][index2+1:].rstrip()

print(mydict)