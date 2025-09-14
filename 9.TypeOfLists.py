# Los arrays son listas que pueden almacenar multiples valores en una sola variable

food = ["pizza", "hamburguesa", "perro caliente", "ensalada"]

food.append("helado")  # agrega al final
food.remove("ensalada") # elimina el elemento indicado
food.pop()  # elimina el ultimo elemento
food.insert(0, "tacos")  # inserta en la posicion indicada
food.sort()  # ordena alfabeticamente
food.clear()  # limpia la lista

for x in food:
    print(x)

#2D arrays
drinks = ['espresso', 'latte', 'cappuccino']
dinner = ['pizza', 'pasta', 'salad']
dessert = ['tiramisu', 'gelato']

food = [drinks, dinner, dessert]

print(food[0][1])  # latte

#---------------------------------------------------------------------------------------------------------

# Las tuplas son inmutables, no se pueden cambiar, agregar o eliminar elementos despues de creadas

student = ("bro", 21, "male")

print(student.count("bro"))
print(student.index(21))

for x in student:
    print(x)

if "bro" in student:
    print("yes, 'bro' is in the student tuple")

#---------------------------------------------------------------------------------------------------------

# Las sets son colecciones desordenadas de elementos unicos

utensils = {"fork", "spoon", "knife"} 
dishes = {"bowl", "plate", "cup"}

utensils.add("napkin") # Agrega un elemento al set
utensils.remove("fork") # Elimina un elemento del set
utensils.clear(dishes) # Elimina todos los elementos del set
utensils.update(dishes) # Agrega los elementos de un set a otro set
dinner_table = utensils.union(dishes) # Une dos sets en uno nuevo

print(utensils.difference(dishes)) # Muestra los elementos que estan en un set pero no en el otro
print(utensils.intersection(dishes)) # Muestra los elementos que estan en ambos sets

for x in utensils:
    print(x)

for x in dinner_table:
    print(x)

#---------------------------------------------------------------------------------------------------------

# Diccionarios (key-value pairs)

capitals = {'USA': 'Washington DC', # clave: valor
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow',}

capitals.update({'Germany': 'Berlin'}) # agrega un nuevo par clave-valor
capitals.update({'USA': 'Las Vegas'})  # actualiza el valor de la clave indicada
capitals.pop('China')  # elimina el elemento con la clave indicada
capitals.clear()  # elimina todos los elementos del diccionario

print(capitals['Russia']) # accede al valor de la clave indicada
print(capitals.get('India')) 
print(capitals.keys()) # accede a todas las claves
print(capitals.values()) # accede a todos los valores
print(capitals.items()) # accede a todos los pares clave-valor

for key, value in capitals.items():
    print(key, value)