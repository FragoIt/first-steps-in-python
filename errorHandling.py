import string
from tokenize import String


def divisor(numero):
    my_list=[]
    for i in range(1,numero + 1):
        if numero%i==0:
            my_list.append(i)

    
    return my_list



while True:
    try:
        numero=int(input('INGRESA EL MALPARIDO VALOR, QUE TE CUESTA, MISERABLE '))
        break
    except:
        print('ingrese EXCLUSIVAMENTE números, por favor')        
            
print(divisor(numero))   
              