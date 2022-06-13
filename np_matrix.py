

import numpy as np
import random
from random import shuffle
# array1 = np.array([88, 23, 39, 41])
# array2 = np.array([[76.4, 21.7, 38.4], [41.2, 52.8, 68.9]])
# array3 = np.array([[12], [4], [9], [8]])
# balotas = ["B1", "B2", "B15", "I16", "I17",, "I30",
# "N31", "N32", …, "N45", "G46", "G47", …, "G60", "O61", "O62",]

# def generate_card():
    

def generador():
    card = {
        "B": [],
        "I": [],
        "N": [],
        "G": [],
        "O": [],
    }
    
    min = 1
    max = 16
    for letter in card:

        card[letter] =list(np.arange(min, max))
        min += 15
        max += 15
    #texto_plano= list(card.items())
    baloto=[]
    for key, value in card.items():
    
        for number in value:
            aux= str(number)
            baloto.append(key + aux)
    return baloto

    # print(texto_plano[4])
    # print(card.keys(),'\n')
    # print(card.values())
    



def balotera(balotas):
    blend=[]
    balotas_revueltas=[]   
    selection= []
    blend=np.array_split(balotas,5)
    '''
    [
        [B] INDICE 0
        [I] INDICE 1
        [N] INDICE 2
        [G] INDICE 3
        [O] INDICE 4  
    ]
    
    '''
    
    
    for i in blend:
        if i not in blend[2]:
            selection.append(random.choices(i,k=5))
        if len(selection) >25:
            break

    selection.insert(2, random.choices(blend[2],k=4))        
    for lista in selection:
        for elemento in lista:
            balotas_revueltas.append(elemento)    
            
    random.shuffle(balotas_revueltas)
    balotas_revueltas= tuple(balotas_revueltas)        
    return  balotas_revueltas
    


        


entry= generador()
#print(balotera())
balotas_revueltas= balotera(entry)
print(balotas_revueltas)