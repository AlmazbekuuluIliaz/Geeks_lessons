data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for item in data_tuple:
    if isinstance(item, str):
        letters.append(item)
    else:
        numbers.append(item)
numbers.remove(6.13)
letters.insert(len(letters), letters.pop(letters.index(True)))
letters.insert(letters.index(3) + 1, 2)
numbers = sorted(numbers)
letters.reverse()
letters[1] = 'G'
letters[4] = 'c'
numbers = [num ** 2 for num in numbers]
numbers_tuple = tuple(numbers)
letters_tuple = tuple(letters)