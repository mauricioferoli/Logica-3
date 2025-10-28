contador=0

while True:
    contador=contador+1
    print(contador)
    resp=input("X para detener").uppper()
    if resp=="X":
        break
print(f"Contador {contador}")