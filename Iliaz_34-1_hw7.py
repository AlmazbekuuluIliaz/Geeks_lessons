ten = list(range(1, 10))
evens = list(filter(lambda x: x % 2 == 0, ten))
squared_evens = list(map(lambda x: x ** 2, evens))

def display_item_at_index(lst=None):
    if lst is None:
        lst = list(range(1, 10))  # Создание списка от 1 до 10
    
    while True:
        try:
            index = int(input("enter index: "))
            if index == -1:
                print("completed.")
                break
            
            if 0 <= index < len(lst):
                print(f"element with index {index}: {lst[index]}")
            else:
                print(f"index {index} unacceptabled. enter index from 0 to {len(lst)-1}.")
        except ValueError:
            print("something wrong!")


display_item_at_index(ten)
print("Список квадратов четных чисел:", squared_evens)

