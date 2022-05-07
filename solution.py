"""
NO ELIMINAR LAS SIGUIENTES IMPORTACIONES, 
El equipo de desarrollo de este calificador modificó las funciones 'print' e 'input'.
Esta modificación se hizo con la finalidad de que el sistema pueda calificar tu solución.
Por eso LEER MUY BIEN LO QUE SE SOLICITA Y LAS RESTRICCIONES QUE SE LE IMPUSIERON A ESTAS DOS FUNCIONES.
"""
#from student_utilities import input, print


from ast import If
from operator import truediv


def solucion():
    # ACÁ INICIA LA FUNCIÓN SOLUCIÓN (En este espacio debes entregar tu solución)

    total_a_cobrar= 0
    sub_total= 0
    bandera= True

    while bandera:
        valor_producto = int(input("Ingrese el valor unitario: "))
        producto_iva=input("¿El producto cuenta con IVA? s/n")
        
        numeros_de_productos= int(input(" ingrese la Cantidad del producto a registrar? "))
        if producto_iva == "s":
            print("IVA incluído")
            #iva= valor_producto * 0.19
            producto_total_iva= valor_producto + (valor_producto * 0.19)
        elif producto_iva== "n":
            print("PRODUCTO SIN IVA")
            producto_total_iva= valor_producto
        if numeros_de_productos >=1:
            sub_total+= producto_total_iva * numeros_de_productos
        
        print(f'SUBTOTAL: {sub_total}')
        productos_faltantes= input("¿Faltan productos por cobrar? S/N ")
        if productos_faltantes== "s":
            continue
        elif productos_faltantes== "n":
            total_a_cobrar = sub_total
            print(f"TOTAL A COBRAR : {total_a_cobrar}")
            bandera= False

solucion()
                
        



    
            



            




