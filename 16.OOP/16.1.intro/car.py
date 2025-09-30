class Car:

    wheels = 4 #Variable de clase


    def __init__(self,make,model,year,color):
        self.make = make    #Variable de instancia
        self.model = model  #Variable de instancia
        self.year = year    #Variable de instancia
        self.color = color  #Variable de instancia

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopping")