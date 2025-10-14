import random
cant_inscritos=random.randint(0,10)
print(cant_inscritos)
if cant_inscritos>7:
    print("Comenzará el curso")
    print("porque hay ", cant_inscritos, "inscritos")
if cant_inscritos<=8:
    print("No comenzará porque no se cubrió la matrícula mínima")
