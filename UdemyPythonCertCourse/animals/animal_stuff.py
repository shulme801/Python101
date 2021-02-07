class Animal:

    def __init__(self, name):
        self.animal_name = name

    def eat(self):
        raise NotImplementedError("Child class should be implementing this abstract method")

class Monkey(Animal):
    
    def eat(self):
        print("money eating bananas")

class Bird(Animal):
    
    def eat(self):
        print("bird eating seeds")

    def fly(self):
        print("bird soaring high")

    def talk(self):
        print("you are a dork!")

myMonkey = Monkey("jojo")
mango   = Bird("Mango")
mango.talk()

myMonkey.eat()


