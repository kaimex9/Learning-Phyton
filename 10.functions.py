# Estas son las funciones en Python

def hello(v1,v2,v3): #aqui definimos la funcion 
    print("Hello " + v1 + " your name is " + v2)
    print("and you are " + str(v3) + " years old") 

name = "Alex"
age = 21
hello("bro", name, age) #aqui llamamos a la funcion

#-----------------------------------------------------------
# Funciones con valor de retorno

def multiply(v1,v2):
    result = v1 * v2
    return result #aqui hacemos que la funcion devuelva un valor

x = multiply(2,3) #aqui llamamos a la funcion

print(x) #aqui imprimimos el valor devuelto por la funcion

#-----------------------------------------------------------
# Funciones con argumentos nombrados (no importa el orden)

def hello(first, middle, last): #aqui definimos la funcion
    print("Hello " + first + " your middle name is " + middle + " and your last name is " + last)

hello(last="code", middle="is", first="this") #aqui llamamos a la funcion con argumentos nombrados

#-----------------------------------------------------------
# Esto son args (argumentos por defecto)

def add(*stuff): #aqui definimos la funcion con argumentos por defecto
    sum = 0
    stuff = list(stuff) # Convertir la tupla a lista para poder modificarla
    stuff[0] = 10
    for x in stuff: #aqui recorremos los argumentos
        sum += x
    return sum

print(add(1,2,3))

#-----------------------------------------------------------
# Esto son kwargs (argumentos nombrados por defecto)

def hello(**kwargs): #aqui definimos la funcion con argumentos por defecto
    print("Hello " + kwargs['first'] + " " + kwargs['middle'] + " " + kwargs['last'])
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(key + " : " + value , end=" ") # end=" " hace que no se haga un salto de linea


hello(first="Alex", middle="is", last="code") #aqui llamamos a la funcion con argumentos nombrados