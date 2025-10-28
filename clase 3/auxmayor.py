
auxiliar_mayor=0
while True:
    dato=int(input("Ingrese edad-> "))
    if dato>auxiliar_mayor :
        auxiliar_mayor=dato
    print(f"El mayor hasta el momento es {auxiliar_mayor}")
    resp=input("Presione x para detener el programa").lower()
    if resp=="x":
        break

print(f"\nEl mayor es {auxiliar_mayor}")