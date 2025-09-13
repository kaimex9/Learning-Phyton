x = 10 #int
y = 3.14 #float
z = "3" #str

x = float(x)  # Convertir int a float
y = int(y)  # Convertir float a int
z = int(z)  # Convertir str a int

print(x)
print(y)
print(z*2)  # Multiplicar z por 2 después de convertirlo a int

name = input("cual es tu nombre?")
age = int(input("cual es tu edad?"))

age += 1  # Incrementar la edad en 1

print("muy buenas " + name + ", tienes " + str(age) + " años")



import math
pi = 3.14
x = 1
y = 2
z = 3

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi,2))
print(math.sqrt(420))
print(max(x,y,z))
print(min(x,y,z))