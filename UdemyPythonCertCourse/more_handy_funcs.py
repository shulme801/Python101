list_a = ['a', 'b', 'c', 'd','e', 'f']
list_b = [1, 2, 3, 4, 5, 6]
list_c = [99, 98, 97, 96, 95, 94]

zipped_list = list(zip(list_a, list_b, list_c))

for (a, b, c) in zipped_list:
    print(a)
    print(b)
    print(c)


print('z' in list_a)
print()
name = input('Enter your name: ')
print("Hello there " + name.strip())
print()
number = input('Enter your number: ')
print(55 + int(number))



