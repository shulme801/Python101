# Stephen H. Hulme  8 Nov 2020
# Basic work with lists.  Experiments are commented out

motorcycles = []
motorcycles.append('honda')
motorcycles.append('harley davidson')
motorcycles.append('ducati')
# motorcycles.append(14) This works b/c you can have a list with heterogenous types.  This stmt adds an integer to the 
# end of the list

motorcycles.insert(0,'indian')
myMSG = (", ".join(motorcycles)).title()
print(myMSG)
too_expensive = ('ducati')
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me")

# print(motorcycles[-1].title())  assuming the last item in the list is a variable of type string, this prints the last item 
# with Title capitalization
# print(motorcycles.title()) should get an error because a list object has no "title" attribute.

# motorcycles.append(14)
# print(motorcycles[-1])
