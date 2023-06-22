def calculate():
    print('Выберите операцию')
    print('* - умножение')
    print('/ - деление')
    print('+ - сложение')
    print('- - вычитание')
    print('D - дискриминант')
    print('Введите % для выхода')

    operation = input()

    if operation == '*':
        num1 = input('Введите 1 число: ')
        num2 = input('Введите 2 число: ')
        try:
            res = int(num1) * int(num2)
        except ValueError:
            print('Неизвестное значение')
        else:
            print(res)
    elif operation == '/':
        num1 = input('Введите 1 число: ')
        num2 = input('Введите 2 число: ')
        try:
            res = int(num1) / int(num2)
        except ValueError:
            print('Неизвестное значение')
        else:
            print(res)
    elif operation == '+':
        num1 = input('Введите 1 число: ')
        num2 = input('Введите 2 число: ')
        try:
            res = int(num1) + int(num2)
        except ValueError:
            print('Неизвестное значение')
        else:
            print(res)
    elif operation == '-':
        num1 = input('Введите 1 число: ')
        num2 = input('Введите 2 число: ')
        try:
            res = int(num1) - int(num2)
        except ValueError:
            print('Неизвестное значение')
        else:
            print(res)
    elif operation == 'D':
        num1 = input('Введите 1 число(a): ')
        num2 = input('Введите 2 число(b): ')
        num3 = input('Введите 3 число(c): ')
        try:
            res = int(num2)**2 - 4 * int(num1) * int(num3)
        except ValueError:
            print('Неизвестное значение')
        else:
            print(res)
    elif operation == '%':
        exit()
    else:
        print('Неизвестная операция! Повторите попытку.')
    print(" ")

    calculate()

calculate()