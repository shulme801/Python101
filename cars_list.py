cars = ['bmw', 'lexus', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars = ['bmw', 'lexus', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
#
#Now, play with the sorted() function
cars = ['bmw', 'lexus', 'audi', 'toyota', 'subaru']
print('Here is the original list:')
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))
print('\nHere is the reverse sorted list:')
print(sorted(cars,reverse=True))
print('\nHere is the original list again:')
print(cars)
cars.reverse()
print(cars)
print(len(cars))
