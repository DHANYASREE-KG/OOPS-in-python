#Single inheritance

class Vehical: #parent class
    No_of_wheels=4
    def moveforward(self):
        print("vehicle is moving forward")
    
class Car(Vehical): #child class
    No_of_airbags=3

a=Car()
print(a.No_of_wheels)
print(a.No_of_airbags)
a.moveforward()

#Hierachial inheritance

class Vehical: #parent class
    No_of_wheels=4
    def moveforward(self):
        print("vehicle is moving forward")
    
class Car(Vehical): #child class
    No_of_airbags=3

class Bike(Vehical): #child class
    No_of_chains=10

b=Bike()
print(b.No_of_wheels)
print(b.No_of_chains)
#print(b.No_of_airbags) #this will give error because bike class does not have No_of_airbags attribute
b.moveforward()

#Multilevel inheritance

class Vehical: #parent class
    No_of_wheels=4
    def moveforward(self):
        print("vehicle is moving forward")
    
class Car(Vehical): #child class
    No_of_airbags=3

class Bike(Car): #child class
    No_of_chains=10

c=Bike()
print(c.No_of_wheels)
print(c.No_of_airbags)
print(c.No_of_chains)
c.moveforward()

# Multiple inheritance

class Father:
    hair_color="black"
class Mother:
    hair_color="brown"
    eye_color="blue"
class Child(Father,Mother):
    no_of_legs=2
d=Child()
print(d.hair_color)
print(d.eye_color)
print(d.no_of_legs)

#Diamond problem
class Vehical: #parent class
    No_of_wheels=4
    def moveforward(self):
        print("vehicle is moving forward")
    
class Car(Vehical): 
    No_of_airbags=3

class Maruthi(Car): 
    millage=20

class Toyota(Car):
    millage=15

class Innova(Maruthi,Toyota):
    has_touchscreen=True

e=Innova()
print(e.No_of_wheels)
print(e.No_of_airbags)
print(e.millage)
print(e.has_touchscreen)
e.moveforward()