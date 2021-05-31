#from abc import ABC,abstractmethod
class Animal(ABC):
    def move(self):
        pass


class Human(Animal):
    def move(self):
        print("i can walk and run")

class Monkey(Animal):
    def move(self):
        print("I jump and dance")

R=Human()
R.move()
M=Monkey()
M.move()