"""courses = ["Python", "JavaScript", "Ruby", "Java", "C#"]
new_courses = ["HTML", "CSS", "Django"]

#new_list = courses [0:3]
#print(new_list)

# Metodos de listas
# append, metodo para añadir al final de la lista
# insert, metodo para añadir en una posicion especifica
# remove, metodo para eliminar un elemento de la lista y pop para eliminar por posicion
# extend, metodo para extender la lista con otra lista
# in para verificar si un elemento esta en la lista y index para obtener la posicion de un elemento



courses.append("Go")
courses.insert(2, "PHP")
courses.remove("Ruby")
courses.extend(new_courses)

print(courses)

Otros metodos son:
Copy: para copiar una lista
reverse: para invertir una lista
sort: para ordenar una lista
clear: para limpiar una lista

copy_list = courses.copy()
print(copy_list)

reversed_list = list(reversed(courses))
print(reversed_list)"""