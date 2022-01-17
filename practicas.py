hero_age = 0
name = "Vanesa"

def asignar_edad():
    global hero_age 
    hero_age += 1

def asignar_nuevo_nombre():
    name = "Sofía"
    return name

new_name = asignar_nuevo_nombre()

asignar_edad()
asignar_edad()
asignar_edad()
asignar_edad()
asignar_edad()
asignar_edad()

print(name)
print(hero_age)

