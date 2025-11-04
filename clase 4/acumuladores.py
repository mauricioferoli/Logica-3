
total_acumulado=0 #acumulador de todos los profesores
cant_prof=0
while True:
    cant_prof=cant_prof+1
    print("*"*25)
    nombre=input("Como se llama la materia?")
    monto_prof=0 #acumulador de cada profesor
    cant_materias=0
    while True: 
        cant_materias=cant_materias+1
        materia=input("Nombre de la materia -> ")
        costo=float(input("Cual es el costo de la materia? -> "))
        monto_prof=monto_prof+costo
        resp=input("X para continuar con otro profesor").upper()
        if resp=="X":
            break
    total_acumulado=total_acumulado+monto_prof
    prom_prof=monto_prof/cant_materias
    print(f"El profesor {nombre} percibe {monto_prof} por todas las materias")
    print(f"siendo un promedio de {prom_prof}")
    print("*"*25)
    detener=input("Presione espacio para ver estadisticas generales").upper()
    if detener==" ":
        break
promedio_=total_acumulado/cant_prof
print(f"El costo por materias de todos los profesores es {total_acumulado}")
print(f"Los profesores ganan en promedio {promedio_}$")