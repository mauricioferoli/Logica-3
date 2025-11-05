def promediar(sumatoria, cantidad_variables):
    if cantidad_variables>0:
        prom=sumatoria/cantidad_variables
    else:
        prom=0
    return prom

def porcentaje(cont_est, cont_g):
    if cont_g>0:
        porc=cont_est/cont_g*100
    else:
        porc=0
    return porc

def calcular(acum_gen, acum_aprob, acum_reprob, cant_est, cant_aprob, cant_reprob):
    promediog=promediar(acum_gen, cant_est)
    promedio_aprob=promediar(acum_aprob, cant_aprob)
    promedio_reprob=promediar(acum_reprob, cant_reprob)
    porc_aprob=porcentaje(cant_aprob, cant_est)
    porc_reprob=porcentaje(cant_reprob, cant_est)
    return promediog, promedio_aprob, promedio_reprob, porc_aprob, porc_reprob

def imprimir(prom_g, prom_aprob, prom_reprob, porc_ap, porc_rep):
    print(f"Promedio general {round(prom_g)}")             #round fue agregado como extra
    print(f"Promedio aprobados {round(prom_aprob)}")       #round fue agregado como extra
    print(f"Promedio reprobados {round(prom_reprob)}")     #round fue agregado como extra
    print(f"De {cant_est} estudiantes, {cant_aprob} aprobaron y {cant_reprob} reprobaron")
    print(f"Siendo {round(porc_ap,2)}% aprobados y {round(porc_rep,2)}% reprobados")

#Cuerpo Principal
acum_aprob=0
acum_reprob=0
cant_aprob=0
cant_reprob=0
cant_est=0
acum_gen=0
while True:
    cant_est=cant_est+1
    nota=float(input("Cuanto saco el estudiante?"))
    if nota>79:
        cant_aprob=cant_aprob+1
        acum_aprob=acum_aprob+nota
    if nota<80:
        cant_reprob=cant_reprob+1
        acum_reprob=acum_reprob+nota
    acum_gen=acum_gen+nota
    resp=input("X para detener el ciclo").upper()
    if resp=="X":
        break

prom_g, prom_aprob, prom_reprob, porc_ap, porc_rep=calcular(acum_gen, acum_aprob, acum_reprob, cant_est, cant_aprob, cant_reprob)
imprimir(prom_g, prom_aprob, prom_reprob, porc_ap, porc_rep)
