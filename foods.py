# Fun with lists
# Stephen H Hulme
# Nov 21, 2020
#
print('#########')
# The following won't do what you think it will
my_foods = ['pizza', 'falafel', 'carrot cake', 'pie']
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")

for food in my_foods[:]:
    print(food.title())
print('\n')

print("My friend's favorite foods are:")
for food in friend_foods[:]:
    print(food.title())
print('\n')
# Now, try using a slice to copy my_foods to friend_foods. We get two separate lists
print('#########')
my_foods = ("")
my_foods = ['pizza', 'falafel', 'carrot cake', 'pie']
friend_foods2 = my_foods[:]
my_foods.append('cannoli')
friend_foods2.append('ice cream')
print("\nNow, my favorite foods are:")
for food in my_foods[:]:
    print(food.title())
print('\n')
print("Now, My friend's favorite foods are:")
for food in friend_foods2[:]:
    print(food.title())
print('\n')
