
auxiliar_menor=96
while True:
    dato=int(input("Ingrese edad-> "))
    if dato<auxiliar_menor :
        auxiliar_menor=dato
    print(f"El menor hasta el momento es {auxiliar_menor}")
    resp=input("Presione x para detener el programa").lower()
    if resp=="x":
        break

print(f"\nEl menor es {auxiliar_menor}")