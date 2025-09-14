# Los bucles for sirven para recorrer un rango de numeros o cadenas de texto

import time #Importamos la libreria time para usar time.sleep()

for i in range(10): #Un bucle for standar del 0 al 9
    print(i+1)
 
for i in range(50,101,2): #Un bucle for del 50 al 100 de 2 en 2
    print(i)

for i in "Hola Mundo": #Un bucle for que recorre una cadena de texto
    print(i)

for seconds in range(10,0,-1): #Un bucle for que cuenta hacia atras de 10 a 1
    print(seconds)
    time.sleep(1)

#---------------------------------------------------------------------------------

rows = int(input("Ingresa el numero de filas: ")) #Pide al usuario el numero de filas
columns = int(input("Ingresa el numero de columnas: ")) #Pide al usuario el numero de columnas
symbol = input("Ingresa el simbolo a usar: ") #Pide al usuario el simbolo a usar

for i in range(rows): #Bucle for para las filas
    for j in range(columns): #Bucle for para las columnas
        print(symbol, end="") #Imprime el simbolo sin salto de linea
    print() #Salto de linea despues de cada fila

phone_number = input("625-555-1234")

for i in phone_number:
    if i == "-":
        continue #Si encuentra un guion, salta a la siguiente iteracion
    print(i, end="")

for i in range(1, 21):
    if i == 13:
        pass #Si encuentra el 13, no hace nada y continua
    else:
        print(i)