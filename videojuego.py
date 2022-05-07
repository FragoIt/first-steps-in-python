
from random import randint


def run():
    num_cualquiera = randint(1, 100)
    cerca = True
    lejos = 0

    while cerca== True :
        numero = int(input('ingrese un numero del 1 - 100 '))
        if numero <num_cualquiera :
            print('digite un numero mayor')
            
        elif numero>num_cualquiera:
            print('digite un valor menor a este')
            
        elif numero== num_cualquiera:
            print('MRK TE LO GANASTE!')
            cerca=False




if __name__== "__main__":   
    run()         


