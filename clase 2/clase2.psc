subProceso capturard(nombre, mventas, cant)
	mostrar "Como te llamas?"
	leer nombre
	mostrar "Cual fur tu monto de ventas?"
	leer mventas
	mostrar "Cuantos autos vendiste?"
	leer cant
FinSubProceso
subProceso calcular(cant, mventas, comision, comisionv, salario)
	sbase=120000
	comisionv=mventas*0.18
	comision=cant*30000
	salario=sbase+comisionv+comision
FinSubProceso
SubProceso imprimir_(nombre, comision, comisionv, salario)
		mostrar "Empleado: " nombre		
		mostrar "Comision por autos: " comision		
		mostrar "Comsion por ventas: " comisionv
		mostrar "Salario Final: " salario
FinSubProceso
Algoritmo 
	
FinAlgoritmo
	