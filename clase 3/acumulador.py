acumulador=0
while True:

    valor=float(input("Cual es el monto?"))
    acumulador=acumulador+valor #Actualizacion del acumulador

    resp=input("X para detener").upper()
    if resp=="X":
        break
print(f"El total acumulado es {acumulador}")