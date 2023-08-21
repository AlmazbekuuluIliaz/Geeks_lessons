# Функции, аргументы: *args, **kwargs.
# DRY - DON'T REPEAT YOURSELF

"""схема функции"""
# определение наименование(параметры):
#     тело функции
#     возвращение результата
    
# наименование(аргументы)

# apples = [1, 1, 1, 1, 1, 1, 1, 1]

# def len1(items):
#     counter = 0
#     for i in items:
#         counter += 1
#     return counter
# # counter = 0
# # for i in apples:
# #     counter += 1
# # print(counter)

# print(len1(apples))
# print(len(apples))

# def get_square(width, length):
#     return width * length
# square_2 = get_square(5, 7)
# square_hall = get_square(10, 15)
# print(square_2, square_hall)

# def get_square(width, length):
#     """
#     Функци принимает ширину и длину, затем возвращает площадь их!
#     """
#     return width * length
# print(get_square.__doc__)
# def greet(name, surname): # name - required positional parameter
#     print(f'Hello name: {name}, surname: {surname}')
# greet(name='Argen', surname='Bekturov') # required positional argument, keyword arguments
# greet('Timur')
# greet('Azat')

# def menu(**kwargs):
#     return kwargs

# monday = menu(eat='pizza', drink='tea', r=4, u=7)
# print(monday)
# print(min([45, 67, 23, 73]))
# print(max([45, 67, 23, 73]))
# print(sum([45, 67, 23, 73]))


# def plus(*args):
#     print(args)
#     return sum(args)

# print(plus(2, 3, 6, 7, 56, 34))

numbers_list = [45, 67, 23, 73]
def find_min(numbers):
    return min(numbers)
print(find_min(numbers_list))

numbers_list = [45, 67, 23, 73]
def find_max(numbers):
    return max(numbers)
print(find_max(numbers_list))

numbers_list = [45, 67, 23, 73]
def find_sum(numbers):
    return sum(numbers)
print(find_sum(numbers_list))