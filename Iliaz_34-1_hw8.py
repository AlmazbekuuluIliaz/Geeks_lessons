data = {}
with open('results.txt', 'r', encoding='utf-8') as file:
    for i in file:
        name, score = i.strip().split(',') # name - ключ, score - значение
        data[name] = int(score)

min_data = dict(sorted(data.items(), key=lambda item: item[1]))

print("Топ-3 лучших студента:") # тут у нас крч вывод топа 3
count = 0
for name, score in min_data.items():
    print(f"{name}: {score}")
    count += 1
    if count == 3:
        break

with open('sorted_results.txt', 'w', encoding='utf-8') as file:
    for name, score in min_data.items():
        file.write(f"{name},{score}\n")

