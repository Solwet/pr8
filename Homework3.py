def base13(number):
    base13_numbers = "0123456789ABC"
    
    if number == 0:
        return "0"
    
    if number < 0:
        return "-" + base13(-number)
    
    if number < 13:
        return base13_numbers[number]
    
    return base13(number // 13) + base13_numbers[number % 13]

number = int(input("Введите десятичное число: "))
translate_number = base13(number)
print("Число в тринадцатиричной системе: " + translate_number)