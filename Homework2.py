while True:
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        result = a + b
        
        print("Сумма чисел: " + str(result))
    
    except ValueError:
        print("Ошибка: введите целые числа!")