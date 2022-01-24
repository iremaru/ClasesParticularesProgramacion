# Áreas --> funciones de las áreas por parámetros
# MENÚ 
def area_rectangulo(base,altura):
    arear= base*altura
    print(f"El área del rectángulo es {arear}.")

def area_triangulo(base,altura):
    areat= (base*altura)/2
    print(f"El área del triangulo es {areat}.")

def area_circulo(radio):
    areac= (2 * 3.14) * radio
    print(f"El área del círculo es {areac}.")

def area_trapecio(base_menor,base_mayor,altura):
    areat= ((base_menor + base_mayor)/2) * altura
    print(f"El área del trapecio es {areat}.")

esta_ejecutandose = True

while (esta_ejecutandose):
    #Texto de información para el usuario
    print("/-----------------------------------/")
    print(f"Indica la operación a realizar: ")
    print (f"Opción 1: Área de un rectángulo")
    print (f"Opción 2: Área de un triángulo")
    print (f"Opción 3: Área de un círculo")
    print (f"Opción 4: Área de un trapecio")
    print (f"Opción 5: Salir")
    print("/-----------------------------------/")
    #fin del texto de información
    
    opcion = int(input(f"La opción elegida es: "))

    if (opcion == 1):
        base= int(input(f"Indique la base: "))
        altura= int(input(f"Indique la altura: "))
        area_rectangulo(base,altura)
    
    elif (opcion == 2):
        base= int(input(f"Indique la base: "))
        altura= int(input(f"Indique la altura: "))
        area_triangulo(base,altura)
    
    elif (opcion == 3):
        radio= int(input(f"Indique el radio: "))
        area_circulo(radio)
    
    elif (opcion == 4):
        base_menor= int(input(f"Indique la base menor: "))
        base_mayor= int(input(f"Indique la base mayor: "))
        altura= int(input(f"Indique la altura: "))
        area_trapecio(base_menor, base_mayor, altura)
        
    elif (opcion == 5): 
        esta_ejecutandose = False
        print(f"El programa ha terminado")