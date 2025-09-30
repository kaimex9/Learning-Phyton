#Ejemplo de como utilizar excepciones

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e: #Aqui podemos nombrar a las excepciones con una "e" por ejemplo
    print(e) #Aqui imprimimos por pantalla el error que nos muestre, asi identificaremos donde a saltado el error
    print("You cant divide by zero IDIOT")
except ValueError as e:
    print("Enter only numbers pls")
except Exception as e:
    print("something went wrong")
else: #Si no salta ningun error podemos añadir un else y mostrar el resultado final
    print(result)
finally:
    print("This will always execute")