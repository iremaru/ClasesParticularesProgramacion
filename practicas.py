def calcular_nota(nombre:str, edad, nota):
    if (nota > 5):
        print("Está aprobado") 
    elif (nombre == 'Bonifacio' and nota <8):
        print("Está suspendido")
    elif (edad > 18 and nota >= 4):
        print("Está aprobado")
    elif (nombre == 'Antonio' and nota >=3):
        print("Está aprobado")
    else:
        print("Está suspendido")
    

# alumnos normales
print("/***************************************/")
print("/*******ALUMNOS NORMALES****************/")
print("[] Alumno Jesus, con 16 años y nota 6 debe ser aprobado")
calcular_nota("Jesus", 16, 6)   # Aprobado
print("[] Alumno María, con 16 años y nota 4 debe ser suspendida")
calcular_nota("María", 16, 4)   # Suspe:ndido
print("[] Alumno José, con 16 años y nota 9 debe ser aprobado")
calcular_nota("José", 16, 9)    # Aprobado
print("/***************************************/")
print()

print("/***************************************/")
print("/*******ALUMNOS REPETIDORED****************/")
print("Alumno Alfonso, con 19 años y nota 4 debe ser aprobado")
calcular_nota("Alfonso", 19, 4)   # Aprobado
print("Alumno Bruno, con 20 años y nota 3 debe ser suspendido")
calcular_nota("Bruno", 40, 3)   # Suspenso
print("Alumno Carlos, con 40 años y nota 2 debe ser suspendido")
calcular_nota("Carlos", 40, 2)    # Suspenso
print("/***************************************/")
print()

print("/***************************************/")
print("/*******ALUMNOS ESPECIALES****************/")

print("Alumno Antonio, con 16 años y nota 3 debe ser aprobado")
calcular_nota("Antonio", 16, 3)   # Aprobado
print("Alumno Antonio, con 23 años y nota 3 debe ser aprobado")
calcular_nota("Antonio", 23, 3)   # Aprobado
print("Alumno Bonifacio, con 16 años y nota 8 debe ser aprobado")
calcular_nota("Bonifacio", 16, 8)    # Aprobado
print("Alumno Bonifacio, con 40 años y nota 5 debe ser suspenso")
calcular_nota("Bonifacio", 40, 5)    # Suspenso
print("/***************************************/")