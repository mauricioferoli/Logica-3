def calcular_potencia(base, exp):
    potencia=base*exp
    return potencia

def calcular(num):
    mitad=num/2
    cuartap=mitad/2
    return mitad, cuartap

#Cuerpo principal
num=15
exponente=2
resultado=calcular_potencia(num, exponente)
mitad, cuarta_parte=calcular(num)
print(f"la mitad del numero es {mitad} y su cuarta parte es {cuarta_parte}")
print(f"La potencia del numero es {resultado}")