SubProceso capturad(nombre Por Referencia,mventas Por Referencia,cant Por Referencia)
	Mostrar "Como te llamas?"
	leer nombre
	Mostrar "Cuanto vendiste?"
	leer mventas
	Mostrar "Cuantos autos vendiste?"
	leer cant
FinSubProceso

SubProceso calcular(cant Por Valor,mventas Por Valor,comision Por Referencia,comisionv por referencia,salario Por Referencia)
	sbase=120000
	comisionv=mventas*0.18
	comision=cant*300000
	salario=sbase+comisionv+comision
FinSubProceso

SubProceso imprimir_(nombre por valor,comision por valor,comisionv Por valor,salario Por valor)
	mostrar "Empleado:" nombre
	mostrar "Comision por autos:" comision
	mostrar "Comision por ventas:" comisonv
	mostrar "Salario final:" salario
FinSubProceso

Algoritmo Clase_2
	capturad(nombre,mventas,cant)
	calcular(cant,mventas,comision,comisonv,salario)
	imprimir_(nombre,comision,comisionv,salario)
FinAlgoritmo
//De no definerse el tipo de parametro se asumira como "por valor" en PSeInt//