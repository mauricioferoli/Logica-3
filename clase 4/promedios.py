#INCOMPLETO


def promediar(sumatoria, cantidad_variables):
    if cantidad_variables>0:
        prom=sumatoria/cantidad_variables
    else:
        prom=0
    return prom
def porcentaje(cont_est, cont_g):
    if cont_g>0:
        porc=cont_g
    else:


def calcular(acum_g, acum_aprob, acum_rep, cant_est, cant_aprob, cant_reprob):
    promediog=promediar(acum_gen/cant_est)
    promedio_aprob=promediar(acum_aprob/cant_aprob)
    promedio_reprob=promediar(acum_reprb/cant_reprob)
    porc_aprob=cant_aprob/cant_est*100
    porc_reprob=cant_reprob/cant_est*100
    return promediog, promedio_aprob, promedio_reprob, porc_aprob, porc_reprob

def imprimir(promediog, promedio_aprob, promedio_reprob, porc_aprob, porc_reprob):
    print(f"Promedio general {promediog}")
    print(f"Promedio aprobados {promedio_aprob}")
    print(f"Promedio reprobados {promedio_reprob}")
    print(f"Porcentaje de aprobados {porc_aprob}")
    print(f"Porcentaje de reprobados {porc_reprob}")  

#Cuerpo Principal
acum_aprob=0
acum_reprb=0
cant_aprob=0
cant_reprob=0
cant_est=0
acum_gen=0
while True:
    cant_est=cant_est+1
    nota=float(input("Cuanto saco el estudiante?"))
    if nota>79:
        cant_aprob=cant_aprob+1
        acum_aprob=acum_aprob+1
    if nota<80:
        cant_reprob=cant_reprob+1
        acum_reprb=acum_reprb+1
    acum_gen=acum_gen+nota
    resp=input("X para detener el ciclo").upper()
    if resp=="X":
        break