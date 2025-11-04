#aqui inicializamos, para contar o acumular entre todas las entidades
mujeres=0
hombres=0
cant_ingles=0
for i in range(3):
    print("Como se llama el prof?")
    nombre=input()
    sexo=input("Ingrese el sexo F/M").upper()
    if sexo=="M":
        hombres=hombres+1
    if sexo=="F":
        mujeres=mujeres+1        
    #aqui inicializamos los contadores para cada profesor
    cant_materias=0
    cant_mat_costosas=0
    while True:
        cant_materias=cant_materias+1
        materia=input(f"Nombre de la Materia -> ").lower()
        costo=float(input("Cual es el costo de la materia?"))
        if costo>500:
            cant_mat_costosas=cant_mat_costosas+1
        if materia=="ingles":
            cant_ingles=cant_ingles+1
        resp=input("X para detener el ciclo").upper()
        if resp=="X":
            break
    porc_mat_costosas=cant_mat_costosas/3*100    
    print(f"El profesor dicta {cant_materias} materias")
    print(f"De las cuales {cant_mat_costosas} son costosas -> {porc_mat_costosas}%")
    print("-"*20)

porc_m=mujeres/3*100
porc_h=hombres/3*100
porc_ingles=cant_ingles/3*100
print(f"Hay {hombres} profesores masculinos {porc_h}%")
print(f"Hay {mujeres} profesores femeninos {porc_m}%")
print(f"Hay {cant_ingles} profesores que dictan ingles {porc_ingles}%")