from random import randint
def bubble_sort(number):
    n = len(number)
    for i in range(n - 1):
        for j in range(n - 1):
            if number[j] > number[j + 1]:
                number[j], number[j + 1] = number[j + 1], number[j]
    return number

number = [25, 42, 99, 100, 461, 62, 1, 20, 56, 07]
print(sorted_list)

def binary_search(val, sorted_list):
    first = 0
    last = len(sorted_list) - 1

    while first <= last:
        middle = (first + last) // 2
        if sorted_list[middle] == val:
            return middle
        elif sorted_list[middle] < val:
            first = middle + 1
        else:
            last = middle - 1
    return -1

val = int(input("Введите число для поиска:"))
index = binary_search(val, sorted_list)

if index != -1:
    print(f'Ваше число найдено в индексе: {index}')
else:
    print("Число не найдено")