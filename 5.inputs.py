# Los inputs se utilizan para recibir datos del usuario a través de la consola.

name = input("Cual es tu nombre?")
age = int(input("Cual es tu edad?"))
height = float(input("Cuanto mides?"))

print("Hola " + name + ", tienes " + str(age) + " años "+ "y mides " + str(height) + " metros")