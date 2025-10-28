contador_a=0
cant_letras=0 #general
while True:
    cant_letras=cant_letras+1
    letra=input("Ingrese la letra -> ").uppper()
    if letra=="A":
        contador_a=contador_a+1
    resp=input("X para detener").uppper()
    if resp=="X":
        break
print(f"Se procesaron {cant_letras} letras")
print(f"Se ingresaron {contador_a} letras A")