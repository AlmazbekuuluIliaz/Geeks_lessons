
color = input("Введите цвет светофора (на английском или русском языке): ").lower()
if color == "красный" or color == "red":
    print("cтойте!")
elif color == "желтый" or color == "yellow":
    print("приготовьтесь!")
elif color == "зеленый" or color == "green":
    print("идите!")
else:
    print("неправильный цвет")