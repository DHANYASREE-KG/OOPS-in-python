#binding data and methods together into a single entity or class is called encapsulation
class Car:
    def __init__(self,no_of_wheels):
        self.__no_of_wheels=no_of_wheels

    #getter method to access private variable __no_of_wheels inside the function they cant be accesed outside the fucntion so thats why the error has got
    def get_no_of_wheels(self):
        print("No of wheels is:",self.__no_of_wheels)

    #setter method to set the value of private variable __no_of_wheels in a controlled way from outside the function
    def set_no_of_wheels(self,no_of_wheels):
        self.__no_of_wheels=no_of_wheels

car1=Car(4)
car1.get_no_of_wheels()
# print(car1.__no_of_wheels)#this will give error because __no_of_wheels is private variable and cannot be accessed outside the class

car1.set_no_of_wheels(6)
car1.get_no_of_wheels()
# print(car1.__no_of_wheels)#this will give error because __no_of_wheels is private variable and cannot be accessed outside the class

