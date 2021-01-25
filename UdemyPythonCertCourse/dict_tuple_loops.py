# employees is a dict
employees = {'mike': 27000, 'john': 65000, 'rebecca': 105000, 'tom': 100000}

for entry in employees.items():
    print(entry)

print("\n\n")

# unpack the dict
for (key, value) in employees.items():
    print('Employee {0} earns {1}'.format(key, value))

print("That's all, folks!\n")

print("\nNext Test -- unpack list of tuples\n")
# Make 'employees' a list of tuples
employees = [('mike', 27000), ('john', 65000), ('rebecca', 105000), ('tom', 100000)]

# unpack the list of tuples
for (key, value) in employees:
    print('Employee {0} earns {1}'.format(key, value))

print("That's all, folks!\n")
