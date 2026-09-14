from abc import ABC,abstractmethod


class Car(ABC):
    @abstractmethod
    def moveforward(self):
        pass

    @abstractmethod
    def movebackward(self):
        pass

    @abstractmethod
    def fm(self):
        pass

class Swift(Car):
    def moveforward(self):
        print("Swift is moving forward")

    def movebackward(self):
        print("Swift is moving backward")

    def fm(self):
        print("Swift FM is playing")

class Baleno(Car):
    def moveforward(self):
        print("Baleno is moving forward")

    def movebackward(self):
        print("Baleno is moving backward")

    def fm(self):
        print("Baleno FM is playing")

swift = Swift()
baleno = Baleno()
swift.moveforward()
baleno.movebackward()
swift.fm()
baleno.fm()

#static method

class math:
    @staticmethod
    def add(a,b):
        return a+b
c=math.add(10,20)
print(c)    