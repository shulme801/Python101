class Employee:
    def __init__(self, name, age):
        self.name  = name
        self.age   = age

    def __str__(self):
        return self.name + " age is " + str(self.age)

    def __len__(self):
        return len(self.name)

John = Employee("John Doe", 47)

print(John)
print(len(John))
