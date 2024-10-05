def homework5():
    sum = 0 
    
    while True:
        a = input("Введите число (или 'stop'/'end' для завершения): ")

        if a.lower() in ["stop", "end"]:
            break
        
        try:
            number = float(a) 
            sum += number
        except ValueError:
            print("Ошибка: пожалуйста, введите число.")
    
    print("Сумма введенных чисел:",sum)

homework5()
