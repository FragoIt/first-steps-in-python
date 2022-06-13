
# total= 1000000
# total_2=0
# bandera=0
# iterable=2
# while total_2<= total:
#     print(f"my mother {2} ** {iterable} == {2 ** iterable} ;;; {total_2}") 
#     total_2= 2** iterable
#     iterable+= 1
from string import ascii_uppercase as alfabeto
#import random


# def encriptador (mensajeSecreto):
#     dicc_I= {}
#     auxiliar={}
#     arreglo_cadena=[]
#     llave={}

#     for i in range(len(mensajeSecreto)):
#         for k in range(len(alfabeto)):
#             if mensajeSecreto[i] in dicc_I:
#                 auxiliar[i]=mensajeSecreto[i]
#             else:  
#                 dicc_I[mensajeSecreto[i]]= alfabeto[i]
    
#     for new in dicc_I.values():
#         arreglo_cadena.append(new)
#     for aux,valor in auxiliar.items():
#         arreglo_cadena.insert(int(aux),valor)

#     mensajeEncriptado= "".join(arreglo_cadena)
#     llave.update(dicc_I)
#     llave['replace']=auxiliar
    
#     print(dicc_I.keys(), '\n', dicc_I.values())
#     print(mensajeEncriptado)        
#     return mensajeEncriptado, llave


# encriptador('dios mio señor salvame') 


def encriptador(mensaje):
    dicci=[]
    encriptado=''
    diccionario= {}
    diccionario[mensaje]=alfabeto
    for i in range(len(diccionario)):
        for caracteres,valor in diccionario.items():
            
        


    # for caracter in range(len(mensaje)):
    #     dicci[mensaje[caracter]]= alfabeto[caracter]
    #     encriptado+= alfabeto[caracter]
    
    # for caracter in range(len(encriptado)):
    #     for k,v in dicci.items():
    #         if k in encriptado[caracter]:
    #             encriptado+= v
                
                    
    print(encriptado)            

encriptador('dios mio')




































  
