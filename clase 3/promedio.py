acum=0
contador=0
while True:
    contador=contador+1
    edad=int(input("Cuantos años tienes?"))
    acum=acum+edad
    resp=input("X para detener").upper()
    if resp=="X":
        break
promedio=acum/contador
print(f"Promedio {promedio}")