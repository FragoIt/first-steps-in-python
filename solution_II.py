def run():
    def loteria (tope,numero_a_adivinar):
        numero_intentos=0
        bandera=True
        chance=int(input(f'Ingrese un valor del 0 hasta el {tope} '))
        while bandera:
           
            if chance<=tope and chance>=0:
                numero_intentos+= 1
                if chance<numero_a_adivinar:
                   chance= int(input('digitame un numero mayor Ma G! \t  '))
                    
                elif chance>numero_a_adivinar:
                    chance= int(input(f'Digitame un numero menor Ma G! \t  '))
                    
                else:
                    print(f'TE LO GANASTE MRKKKK! \n Numero de intentos totales: {numero_intentos} :3')
                    bandera=False

            else:
                chance=int(input('Se salió del intervalo mi rey \t  digite otro numero  '))
                numero_intentos+=0
                
        
    loteria(100,34)        




if __name__== "__main__":
    run()