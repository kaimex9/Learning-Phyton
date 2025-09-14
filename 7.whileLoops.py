# Los bucles while se utilizan para repetir un bloque de código mientras una condición sea verdadera.

text = input("Ingresa tu nombre: ")

while text == "": # Si el usuario no ingresa nada, se le pedirá que ingrese su nombre nuevamente
    text = input("Porfavor introduce un nombre:") 

print("Hola " + text) 

while True:
    name = input("Enter your name: ")
    if name != "":
        break # Si el usuario ingresa algo, se sale del bucle