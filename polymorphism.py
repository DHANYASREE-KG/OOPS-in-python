#poly means many morphism means forms .One method or function have many forms(different things to do) is called polymorphism

#compile time polymorphism: complie code into machine code and if error program doesnt work
""" method overloading: same method name with different parametrs"""

def sum(a,b,c=0):
    return a+b+c
print(sum(2,3))
print(sum(2,3,4))

def sum1(*args):
    total=0
    for i in args:
        total+=i
    print(total)
a=sum1(2,3)

#operator overloading: it is used to perform standard operations on user defined data types. using magic or dunder methods 

class Number:
    def __init__(self,num):
        self.num=num
    def __add__(self,other):
        print(self.num+other.num)
n1=Number(5)
n2=Number(10)
n1+n2

#runtime polymorphism: the code executes correctly in order but crashes at  the middle

#method overriding: same method name with same parameters in parent and child class

class Father:
    def __init__(self):
        print("Father class constructor")
    def say(self):
        print("Hello from father")
class Child(Father):
    def __init__(self):
        print("Child class constructor")
    def say(self):
        print("Hello from child")   
ch=Child()
ch.say()

fa=Father()
fa.say()
