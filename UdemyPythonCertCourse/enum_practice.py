'''
my_nums = [1, 2, 3, 4, 5]
words   = ['hello', 'my', 'name', 'is', 'stephen']

for item in zip(my_nums, words):
    print(item)
'''

my_nums = [1, 2, 3, 4, 5, 6, 7, 8]
words   = ['hello', 'my', 'name', 'is', 'stephen']
for item in zip(my_nums, words):
    print(item)

print("\n\n")
for item in enumerate(words,1):
    print(item)

for i in range(10):
    print(i, end = " ")
print()

for i in range(1,10,2):
    print(i, end = " ")
print()
print("\nThat's all, Folks\n")