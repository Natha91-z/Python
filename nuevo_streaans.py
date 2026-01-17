name = "eduardo"
last_name = "Gracia"

full_name = name + " " + last_name
print(full_name)


full_name = ' '.join([name, last_name])
print(full_name)    

full_name  = 'El nombre completo es: %s %s'  %(name, last_name)
print(full_name)

base = 'El nombre completo es: {} {}. Se edad es: {}'
full_name =  base.format(name, last_name, 30)
print(full_name)    

name = input("Ingresa tu nombre: ")
last_name = input("Ingresa tu apellido: ")  
age = input("Ingresa tu edad: ") 

print(full_name)

