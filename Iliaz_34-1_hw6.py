# первая функция "перемножение чисел"
numbers = (2, 3, 4, 5)

def multiply_numbers(*args):
    result = 1
    for num in args:
        result *= num
    return result
result = multiply_numbers(*numbers)
print("Результат:", result)

# вторая функция "зеркальная строка"
test_string = "level"
def mirror_string(input_str, str = "hello"):
    reversed_str = input_str[::-1]  # Вводим строку

    return reversed_str == input_str
result = mirror_string(test_string)
print(result)  # Выведется True, т.к. "level" читается одинаково в обоих направлениях

# третья функция "калькулятор"
def calculator(num1, action, num2):
    if action == '+':
        return num1 + num2
    elif action == '-':
        return num1 - num2
    elif action == '*':
        return num1 * num2
    elif action == '/':
        if num2 != 0:  # Проверка деления на ноль
            return num1 / num2
        else:
            return "На ноль делить нельзя"
    elif action == '**':
        return num1 ** num2
    elif action == '%':
        return num1 % num2
    
result1 = calculator(2, '**', 3)
print(result1) 

result2 = calculator(5, '+', 9.6)
print(result2)  

result3 = calculator(20, '%', 3)
print(result3) 