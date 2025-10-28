nota_mayor=0
nota_menor=101
n_mayor=""
n_menor=""
while True:
    nombre=input("Como se llama?")
    nota=float(input("Cuanto saco el estudiante -> "))
    if nota>n_mayor:
        nota_mayor=nota
        n_mayor=nombre
    if nota<n_menor:
        nota_menor=nota
        n_menor=nombre
    resp=input("X para detener").upper()
    if resp=="X":
        break
print(f"La nota MAYOR es {nota_mayor} y la obtuvo -> {n_mayor}")
print(f"La nota MENOR es {nota_menor} y la obtuvo -> {n_menor}")