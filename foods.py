my_foods = ['pizza', 'falafel', 'carrot cake', 'pie']
friend_foods = my_foods[:]
print("My favorite foods are:")
my_foods.append('cannoli')
friend_foods.append('ice cream')
# print(my_foods)
for food in my_foods[:]:
    print(food.title())
print('\n')
print("My friend's favorite foods are:")
for food in friend_foods[:]:
    print(food.title())
print('\n')
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
