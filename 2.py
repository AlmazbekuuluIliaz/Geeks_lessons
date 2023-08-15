data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []


# Затем, пройдемся циклом for по кортежу data_tuple и добавим строки в список letters, а все остальные элементы в список numbers:

for item in data_tuple:
    if isinstance(item, str):
        letters.append(item)
    else:
        numbers.append(item)


# Теперь давай из списка numbers удалим число 6.13 и переместим True в конец списка letters, а затем вставим число 2 между 3 и 1:

numbers.remove(6.13)
numbers.append(True)
letters.remove(True)
letters.append(2)


# Далее, отсортируем список numbers, реверсируем список letters и изменим пару букв в letters:

numbers.sort()
letters.reverse()
letters[1] = 'x'
letters[-2] = 'z'


# Теперь давай изменить список numbers, заменив каждое число его квадратом:

numbers = [num ** 2 for num in numbers]


# И, наконец, преобразуем списки numbers и letters в кортежи:

numbers = tuple(numbers)
letters = tuple(letters)