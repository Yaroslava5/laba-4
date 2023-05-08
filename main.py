def p1():
    try:
        a = int(input("Введите число, чтобы проверить деление на 3: "))
        b = a % 3
    except ValueError:
        print("Введено не число!")
    else:
        if b == 0 and a != 0:
            print("Число", a, "делится на 3")
        elif a == 0:
            print("Введён ноль!")
        else:
            print("Число", a, "не делится на 3!")

def p2():
    try:
        a = int(input("Введите число: "))
        b = 100 / a
    except ZeroDivisionError:
        print("Введён ноль!")
    except ValueError:
        print("Введено не число!")
    else:
        print("Результат деления на 100: ", b)

def p3():
    date = input("Введите дату в формате дд.мм.гггг: ")
    date = date.split(".")
    if int(date[0]) * int(date[1]) == int(date[2][2:4]):
        print("дата является магической")
    else:
        print("дата не является магической")


def p4():
    ticket = input("Введите номер билета: ")
    x = 0
    y = 0
    if len(ticket) % 2 == 0:
        for i in ticket[0:int(len(ticket) / 2)]:
            x = x + int(i)
        for i in ticket[int(len(ticket) / 2):int(len(ticket))+1]:
            y = y + int(i)
        if x == y:
            print("Билет счастливый!")
        else:
            print("Билет не является счастливым!")
    else:
        print("Количество цифр нечётно!")
