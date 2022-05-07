from ast import For


numero= int(input('Escribime un número plsss '))
contador_que_cuenta= 0

# if numero% numero== 0 and numero%1==0:
#     print("es un numero prima pai")  
for i in range(1,100):
    if numero%i ==0 and numero%numero==0:
        #print(f'primo pai {numero}')
        contador_que_cuenta+= 1


if contador_que_cuenta==2:
    print('primo mi rey lindo :3') 
else:
    print('no es primo cushita <3')       
            

    
        