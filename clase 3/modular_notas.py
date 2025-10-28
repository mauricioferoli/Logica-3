def capturar_datos():
    nombre=input("Cómo se llama?")
    nota=float(input("Cuánto sacó el estudiante? -> "))
    return nombre,nota
    
def procesar():
    #inicializar las variables auxiliares
    nota_mayor= 0 #menor valor ref
    nota_menor= 100 #mayor valor ref
    n_mayor=""
    n_menor=""
    while True:
        nombre,nota=capturar_datos()
        if nota>nota_mayor:
            nota_mayor=nota
            n_mayor=nombre
        if nota<nota_menor:
            nota_menor=nota
            n_menor=nombre    
        resp=input("X para detener").upper()
        if resp=="X":
            break
    return nota_mayor, n_mayor, nota_menor, n_menor

def imprimir(nota_mayor,n_mayor,nota_menor,n_menor):
    print(f"La nota MAYOR es {nota_mayor} y la obtuvo-> {n_mayor}")
    print(f"La nota MENOR es {nota_menor} y la obtuvo-> {n_menor}")

notamayor, n_mayor,notamenor,n_menor= procesar()
imprimir(notamayor, n_mayor,notamenor,n_menor)