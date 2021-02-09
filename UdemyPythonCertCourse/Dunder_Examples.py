# https://www.geeksforgeeks.org/customize-your-python-class-with-magic-or-dunder-methods/?ref=rp
# declare our own string class 
class String: 
      
    # magic method to initiate object 
    def __init__(self, string): 
        self.string = string 
          
    # print our string object 
    def __repr__(self): 
        return 'Object: {}'.format(self.string) 

    def __add__(self, other):
        return self.string + other
  
# Driver Code 
print ("This file's __name__ is %s" %__name__)
if __name__ == '__main__': 
      
    # object creation 
    string1 = String('Hello') 

    # print object location 
    print(string1) 

    #concatenate String object and a string
    print(string1 + " world!")

class Employee:
    def __init__(self, name, age):
        self.name  = name
        self.age   = age

    def __str__(self):
        return self.name + " age is " + str(self.age)

    def __len__(self):
        return len(self.name)

# John = Employee("John Doe", 47)

# print(John)
# print(len(John))
