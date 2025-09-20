# Asi se utiliza el str.format

animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item) # La forma mas comun de imprimir un texto
print("The {} jumped over the {}".format(animal, item)) # La forma en la que se imprime un texto con str.format
print("The {0} jumped over the {1}".format(animal, item)) # Aqui asignamos ambas variables a posiciones concretas(como un array)
print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) #Aqui prescindimos que las variables y las declaramos dentro de la misma linea

text = "The {} jumped over the {}"
print (text.format(animal,item)) #Podemos hacer lo mismo a traves de un texto almacenado en una variable