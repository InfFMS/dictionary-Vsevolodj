# Напишите программу, которая получает на вход строку чисел, разделенных пробелами, и формирует словарь,
#  в котором ключами служат числа, а значениями – слово "четное" или "нечетное".
keys = str(input())
keys = keys.split()
for j in range(0,len(keys)):
    keys[j] = int(keys[j])
my_dict = dict()
for i in range(0,len(keys)):
    if keys[i]%2==0:
        my_dict[keys[i]] = "Четное"
    else:
        my_dict[keys[i]] = "Нечетное"

print(my_dict[7])