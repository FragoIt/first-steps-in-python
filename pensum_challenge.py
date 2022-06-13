# POR FAVOR LEA TODAS LAS INDICACIONES SUMINISTRADAS EN EL 
# ENUNCIADO ANTES DE EMPEZAR A IMPLEMENTAR SU SOLUCIÓN
from operator import index


pensum=[{1111:{'créditos':4, 'materia':'calculo'}, 1010:{'créditos':2, 'materia':'bases de datos'}}
,{2222:{'créditos':3, 'materia':'matematicas discretas'}}
,{3333:{'créditos':2, 'materia':'bases de datos'},8888:{'créditos':2, 'materia':'bases de datos'}},{},{},{}]


def es_semestre_valido(p, s):
    # ESTA VEZ TU DEFINES TUS RETORNOS
    try:
        if p[s-1] not in p:
            return False
    except:
        flag_2=True
        return False
        
    bandera=len(p)
    bandera_s= int(s)-1
    if p[s-1] not in p:
        return False
    elif s-1 in range(0,len(p)):
        return True
    else:
        return False
    
    
def es_semestre_vacio(p, s):
    # ESTA VEZ TU DEFINES TUS RETORNOS
    if p[s-1]:
        return False 
    else:
        return True


def es_materia_valida(p, s, m):
    # ESTA VEZ TU DEFINES TUS RETORNOS
    if m in p[s-1].keys():
        return True
    else:
        return False    

#vali1,vali2,vali3= es_semestre_valido(),es_semestre_vacio(),es_materia_valida()
def modificar_materia(pensum, semestre, materia, nombre, creditos):
    # ACÁ INICIA LA FUNCIÓN
    pensum[semestre-1][materia]['nombre']=nombre
    pensum[semestre-1][materia]['créditos']=creditos
    
    # ACÁ TERMINA LA FUNCIÓN
    # ESTA VEZ TU DEFINES TUS RETORNOS

def eliminar_materia(pensum, semestre, materia):
    # ACÁ INICIA LA FUNCIÓN
    del pensum[semestre-1][materia]
