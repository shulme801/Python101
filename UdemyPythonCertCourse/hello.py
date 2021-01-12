foobar = "Hello Python World 1/12/2021!"
print(foobar)

print(type(True))
# Python is a dynamically-typed language

answer = 10 + 3 * 9 - 4
print(answer)
answer = (10 + 3) * (9 - 4)
print(answer)

sentence = 'This is a sentence'
print(sentence[0:4])
print(sentence[5:7])
# print(sentence[-2])
sentence = "abcdefg"
print("\n")
print(sentence[0::2])
sen = sentence.upper()
print(sentence)
print(sen)

sentence = "this IS a 99484 sentence"
print(sentence.capitalize())

sentence = "A94848%$3947343983"
print(sentence.startswith("8%$", 5))

sentence = "\nThe sum of {0} + {2} is {1}".format(50, 55, 5)
print(sentence)