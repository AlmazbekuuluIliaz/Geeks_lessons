# lambda функция, работа с исключениями
# lambda arguments: expression

# map, filter

# print('123'[5])
# print(int('dfg'))
# print(34 + 'dfg')
# try:
#     print('34' + '23')
# except:
#     print('error!')
# finally:
#     print('checked!')
    
word = 'python'

while True:
    index_input = int(input('enter index: '))
    print(word[index_input])


# numbers = list(range(1, 21))
# print(numbers)

# filtered_numbers = list(filter(lambda num: num > 9, numbers))
# print(filtered_numbers)

# numbers = list(range(1, 21))
# print(numbers)

# mapped_numbers = list(map(lambda num: num * 10, numbers))
# print(mapped_numbers)

# def up_first_letter(word):
#     return word.title()

# def show_words(func, sequence):
#     for i in sequence:
#         print(func(i))
        
# show_words(len, ['kg', 'python', 'geeks'])
# show_words(up_first_letter, ['tokmok', 'karakol', 'bishkek'])
# show_words(lambda word: word.upper(), ['tokmok', 'karakol', 'bishkek'])

# lambda_func = lambda a, b: a + b
# print(lambda_func(2, 3))

# def lambda_func(a, b):
#     return a + b
# print(lambda_func(2, 3))

# print(type(lambda_func))