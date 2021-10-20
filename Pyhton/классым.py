class Towarm :

    def __init__(self,on_and_off ):
        self.on=on_and_off

    def heat(self,product):
        print(product,' разогревается ')

class Defrost :

    def __init__(self,on_and_off ):
        self.on=on_and_off

    def unfreeze(self,product):
        print(product,' размораживается ')

class Breaking :
    def __init__(self,on_and_off ):
        self.on=on_and_off

    def break_ (self,product):
        print(product,' взорвался вместе с микроволновкой из-за ее неисправности ')

class Microwave(Towarm,Defrost,Breaking):
    
    def __init__(self,on_and_off ):
        self.on=on_and_off

my_class =Microwave('on')
import random
while True:
    productt=input('Введите продукт  ')
    if (input('Хотите разогреть продукт?  ')=='да'):
        my_class.heat(productt)
    if (input('Хотите разогреть продукт?  ')=='да'):
        my_class.unfreeze(productt)
    if (random.randint(0, 1)==1):
        my_class.break_(productt)
