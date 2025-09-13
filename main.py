# CNTRL + K + C para comentar lineas
# CNTRL + K Ctrl + U para descomentar lineas

food = ["pizza", "hamburguesa", "perro caliente", "ensalada"]

food.append("helado")  # agrega al final
food.remove("ensalada") # elimina el elemento indicado
food.pop()  # elimina el ultimo elemento
food.insert(0, "tacos")  # inserta en la posicion indicada
food.sort()  # ordena alfabeticamente
food.clear()  # limpia la lista

for x in food:
    print(x)

