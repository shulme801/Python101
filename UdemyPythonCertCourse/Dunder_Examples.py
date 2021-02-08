class Employee:
    def __init__(self, name, age):
        self.name  = name
        self.age   = age

    def __str__(self):
        return self.name + " age is " + str(self.age)


John = Employee("John Doe", 47)

print(John)