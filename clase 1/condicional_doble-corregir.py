import random
cantidad=int(input("Cuántos productos va a llevar?\n"))
precio=random.randint(1000,50000)
subtotal=precio*cantidad
porc=0
if subtotal>50000:
    porc=0.05
else:   
    porc=0.02
#montodescuento
#total a pagar

#salidas
print("El precio del producto es:", precio)
print("El subtotal de la compra es :", subtotal)
print("EL procentaje de descuento es", porc) 