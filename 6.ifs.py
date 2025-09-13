age = int(input("Cual es tu edad?"))

if age >= 18:
    print("Eres mayor de edad")
elif age == 100:
    print("Eres centenario")
elif age < 0: 
    print("Edad no valida")
else:
    print("Eres menor de edad")
    
    
temp = int(input("Cual es la temperatura?"))

if temp >= 0 and temp <= 30:
    print("La temperatura es agradable")
elif temp < 0 or temp > 30:
    print("La temperatura no es agradable")
    print("No salgas!")