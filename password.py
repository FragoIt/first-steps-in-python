import random
def run():

    def generador_contrasena():
        mayusculas = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
        minusculas = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'n']
        #numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        others_characters = ['_', '.', '-', '&', '$', '?']
        algo = mayusculas + minusculas + others_characters
        value=[]
        print(algo)
        for i in range(15):
            caracter_locochon= random.choice(algo)
            value.append(caracter_locochon)
        
        value=''.join(value)
        return value
        



    contrasena= generador_contrasena()
    print(f'su contraseña ahora es {contrasena}')
if __name__== '__main__':
    run()





