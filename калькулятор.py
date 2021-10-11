def kalculator(a, b, symbol):
    try:
        if symbol == '+':
            print(a+b)
        elif symbol == '/':
            print(a/b)
        elif symbol == '-':
            print(a-b)
        elif symbol == '*':
            print(a*b)
        else:
             print('Ошибка')
    except:
         print('Ошибка')
try: 
    one = int(input('Введите число'))
    two = int(input('А теперь ещё одно'))
    action = input('Выберете действие')
    kalculator(one, two, action)
except:
    print('Ошибка')