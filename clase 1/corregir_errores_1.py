monto=float((input("Cuánto vendiste?\n")))
edad=int((input("Cuántos años tienes?\n")))
sexo=input("Ingrese su sexo f para femenino y m para masculino")

sbase=200
porc=0
bono=0
if monto>0 and monto<75000:
    porc=0.05
elif monto>=90000 and monto<200000:
    porc=0.07
elif monto>=300000 and monto<1000000:
    porc=0.08
elif monto>=1500000:
    porc=0.10
else:
    porc=0.06

if (edad>=55 and sexo.upper=="F") or (edad>=60 and sexo.upper=="M"):
    bono=40000

comision=monto*porc
salariofinal=sbase+comision+bono

print(f"Porcentaje de comisión {porc*100}%")
print(f"comisión obtenida {comision}")
if bono>0:
    print(f"Has obtenido bono de {bono} por ser de la 3ra edad")
print(f"Salario a percibir {salariofinal}")