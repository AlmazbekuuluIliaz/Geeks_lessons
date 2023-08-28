# Работа с файлами.
# w - write
# a - add
# x - не создаст новый файл, если такой существует!
# r - read

with open('new_file.txt', 'r', encoding='utf-8') as file:
    for i in file.read():
        print(i)
    # print(file.read())
    # print(file.readlines()[-1])

# file = open('new_file.txt', 'w', encoding='utf-8')
# file.write('Бишкек, Кыргызстан')
# file.closer()

# with open('new_file.txt', 'a', encoding='utf-8') as file:
#     file.write('Вторая строка!!!')

# with open('new_file.txt', 'x') as file:
#     file.write('3333')
