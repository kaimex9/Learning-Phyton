#Con esto podremos detectar un posible archivo/directorio en el PC

import os

path = "C:\\Users\\Usuario\\Desktop\\test.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exist")

#---------------------------------------------------------------------------------------------------------
#Con esto podemos leer el contenido de un archivo

try:
    with open('C:\\Users\\Usuario\\Desktop\\Learning-Phyton\\test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That field was not found") 

#---------------------------------------------------------------------------------------------------------
#Con esto podemos escribir/sobreescribir en un archivo txt

text = "Hello, this is some text have a good day"

with open('test.txt','w') as file: #Con el parametro '2' podemos sobreescribir el contenido previo
    file.write(text)

with open('test.txt','a') as file: #Con el parametro 'a' podemos añadir texto por encima de el contenido previo
    file.write(text)


#---------------------------------------------------------------------------------------------------------
#Con esto podemos copiar un archivo y renombrarlo a nuestro gusto

import shutil

shutil.copyfile('test.txt','copy.txt') #Con el copyfile podemos hacer una copia y renombrarla a nuestro gusto
shutil.copy2('test.txt','C:\\Users\\Usuario\\Desktop\\copy.txt') #Con el copy2 podemos hacer una copia en una ruta en concreto de nuestro PC

#---------------------------------------------------------------------------------------------------------
#Con esto podemos mover un archivo

import os

source = "test.txt"
destination = "C:\\Users\\Usuario\\Desktop\\test.txt"

try:
    if os.path.exists(destination): #Si aqui detecta que ya hay un archivo llamado "test.txt" devolvera 'true'
        print("There is already a file there")
    else:
        os.replace(source,destination) #En caso contrario movera el archivo indicado a la ruta que queramos
        print(source + " was moved")
except FileNotFoundError:
    print(source + "was not found")

#---------------------------------------------------------------------------------------------------------
#Con esto podemos eliminar un archivo

import os
import shutil

path = "test"
try:
    os.remove(path) #Con esto eliminamos un archivo
    os.rmdir(path) #Con esto eliminamos un directorio
    shutil.rmtree(path) #Con esto eliminamos un directorio que tenga contenido dentro
except FileNotFoundError:
    print("That file was not found")
else:
    print(path + " was deleted")