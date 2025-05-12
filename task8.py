# Представьте, что вы шпионы)
# Придумайте шифр, в котором буквы заменяются на какие-то символы
# и реализуйте шифроватор и дешифроватор

# так как питон не принимает русский алфавит будем делать для строчных букв английского алфавита
str = str(input())
def coder(str):
    a = 34
    alphabet = [chr(i) for i in range(97, 123)]
    alphabet = alphabet + [" "]
    key = [chr(i) for i in range(a, a + 26 + 1)]
    coder = {alphabet[i]: key[i] for i in range(0, len(alphabet))}
    str = list(str)
    text=""
    for i in (str):
        text=text+coder[i]
    return text
def decoder(str):
    a = 34
    alphabet = [chr(i) for i in range(97, 123)]
    alphabet = alphabet + [" "]
    key = [chr(i) for i in range(a, a + 26 + 1)]
    decoder = {key[i]: alphabet[i] for i in range(0, len(alphabet))}
    str = list(str)
    text=""
    for i in (str):
        text=text+decoder[i]
    return text
print(coder(str))
print(decoder(coder(str)))