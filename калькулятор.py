def kalculator(a, b, c):
    '''Функция делает своё дело'''
    try:
        if c == '+':
            print(a+b)
        elif c == '/':
            print(a/b)
        elif c == '-':
            print(a-b)
        elif c == '*':
            print(a*b)
        else:
             print('Ошибка')
    except:
         print('Ошибка')
try: #################
    try: #################
        try: #################
            try: ##################
                one = int(input('Введите число'))
                two = int(input('А теперь ещё одно'))
                action = input('Выберете действие')
                kalculator(one, two, action)
            except:
                print('Ошибка')
        except:
            print('Ошибка')
    except:
        print('Ошибка')
except:
    print('Иди нахуй')
    