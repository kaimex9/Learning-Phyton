#Asi es como se generan valores aleatorios

import random #Importamos la libreria random para poder usar sus funciones

x = random.randint(1,6)

myList = ['rock','paper','scissors']
z = random.choice(myList) #Hacemos que z sea un valor aleatorio de la lista
cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','A'] 

random.shuffle(cards) #Hacemos que los valores de la lista de mezclen de forma aleatoria

print(x)
print(z)
print(cards)