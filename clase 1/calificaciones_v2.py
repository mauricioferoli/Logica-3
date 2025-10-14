def capturardatos():
    global nombre, nota1, nota2, nota3
    print("como te llamas?")
    nombre=input()
    print("Cuales son tus notas?")
    nota1=int(input("Nota 1 ->"))
    nota2=int(input("Nota 2 ->"))
    nota3=int(input("Nota 3 ->"))
    
def imprimir():
    print("-"*30)
    print(f"Hola {nombre}")
    print(f"Tus Notas son: {nota1}-{nota2}-{nota3}")
    print(f"Promedio -> {prom}")
    print("-"*30)

def promediar():
    global prom
    prom=(nota1+nota2+nota3)/3
    if prom>=10:
        print("Aprobado")
    else:
        print("Reprobado")

#Cuerpo Principal
nombre=""
nota1=0
nota2=0
nota3=0
prom=0
capturardatos()
promediar()
imprimir()