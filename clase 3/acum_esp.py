acum_e=0
acumulador=0 #general
while True:
    nombre=input("Como se llama el producto?")
    cant=int(input("Cuantos hay en inventario?"))
    precio=float(input("Cuanto cuesta el producto?"))
    acumulador=acumulador+precio #general
    if cant<5:
        acum_e=acum_e+precio

    resp=input("X para detener").upper()
    if resp=="X":
        break
print(f"Total acumulado de precio cuyos productos en inventario es bajo {acum_e}")
print(f"Acumulado de TODOS los productos {acumulador}")