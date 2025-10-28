def capturard():
	print("Como te llamas?") 
	nombre=input()
	mventas=float(input("Cual fur tu monto de ventas?")) 
	cant=int(input("Cuantos autos vendiste?"))
	return nombre, mventas, cant

def calcular(cant, mventas):
	sbase=120000
	comisionv=mventas*0.18
	comision=cant*30000
	salario=sbase+comisionv+comision
	return comision, comisionv, salario

def imprimir(nombre, comision, comisionv, salario):
    print(f"Empleado: {nombre}") 		
    print(f"Comision por autos: {comision}")
    print(f"Comision por ventas: {comisionv}")
    print(f"Salario Final: {salario}")

def procesar():
    nombre, monto_ventas, cant= capturard()
    comision_autos, comision_ventas, salariof=calcular(cant, monto_ventas)
    imprimir(nombre, comision_autos, comision_ventas, salariof)

#Cuerpo principal
procesar()

#	"Una funcion solo posee pararmetros por valor. Los de referencia vendrian a ser los retornos"
#"En el cuerpo principal cuando llamemos a la funcion debemos asignar a una variable el valor de retorno"