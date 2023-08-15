data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

for item in data_tuple:
    if isinstance(item, str):
        letters.append(item)
    else:
        numbers.append(item)

numbers.remove(6.13)
letters.append(True)
numbers.insert(numbers.index(3) + 1, 2)

numbers.sort()
letters = list(letters)[::-1]
letters[1] = 'G'
letters[7] = 'c'
numbers[1] = 1

numbers = [x**2 for x in numbers]

numbers_tuple = tuple(numbers)
letters_tuple = tuple(letters)

print("letters:", letters_tuple)
print("numbers:", numbers_tuple)