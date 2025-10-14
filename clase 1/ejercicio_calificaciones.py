def saludar():
    print("como te llamas?")
    nombre=input()
    print(f"Hola {nombre}")

def calcular():
    print("Cuales son tus notas?")
    nota1=int(input("Nota 1 ->"))
    nota2=int(input("Nota 2 ->"))
    nota3=int(input("Nota 3 ->"))
    prom=(nota1+nota2+nota3)/3
    print(f"Promedio -> {prom}")

def despedir():
    print("Hasta luego")

#Cuerpo Principal
saludar()
calcular()