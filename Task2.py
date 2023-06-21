#Задача 2:
# Найдите сумму цифр трехзначного числа

a = input("Введите трехзначное число : ")
try:
    b = int(a)
    summ = 0
    l = len(a)
    if l != 3 :
        print('Вы ввели не трехзначное число')
    else:
        while l >= 0:
            summ = summ + int(a) % 10
            a = int(a) // 10
            l = l - 1
        print(f"Сумма цифр числа {b} = {summ}")
except:
    print("Введите трехзначное число !!!")




