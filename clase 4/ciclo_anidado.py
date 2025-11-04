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
    #aqui
    for j in range(5):
        materia=input(f"Nombre de la Materia {j}-> ").lower()
        if materia=="ingles":
            cant_ingles=cant_ingles+1

print(f"Hay {hombres} profesores masculinos")
print(f"Hay {mujeres} profesores femeninos")
print(f"Hay {cant_ingles} profesores que dictan ingles")