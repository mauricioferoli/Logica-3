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
    cont_apr=0
    cont_rep=0
    cantidad=1
    acum_notas=0
    while True:
        cantidad=cantidad+1
        nombre,nota=capturar_datos()
        if nota>nota_mayor:
            nota_mayor=nota
            n_mayor=nombre
        if nota<nota_menor:
            nota_menor=nota
            n_menor=nombre    
        if nota>50:
            cont_apr=cont_apr+1
            print("Aprobado")
        if nota<50:
            cont_rep=cont_rep+1
            print("Reprobado")
        acum_notas=acum_notas+nota
        promedio=acum_notas/cantidad
        resp=input("X para detener").upper()
        if resp=="X":
            break
    return nota_mayor, n_mayor, nota_menor, n_menor, cont_apr, cont_rep, promedio

def imprimir(nota_mayor,n_mayor,nota_menor,n_menor, cont_apr, cont_rep,promedio):
    print(f"Promedio de notas {promedio}")
    print(f"La nota MAYOR es {nota_mayor} y la obtuvo-> {n_mayor}")
    print(f"La nota MENOR es {nota_menor} y la obtuvo-> {n_menor}")
    print(f"Aprobaron {cont_apr}")
    print(f"Reprobaron {cont_rep}")
#Principal   
nota_mayor, n_mayor, nota_menor, n_menor, cont_apr, cont_rep, promedio= procesar()
imprimir(nota_mayor, n_mayor,nota_menor,n_menor,cont_apr, cont_rep, promedio)