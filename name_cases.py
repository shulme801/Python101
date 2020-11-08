first_name = "stephen"
sur_name = "hulme"
full_name = f"{first_name} {sur_name}"
lang = "python"
message = f"Hello, {full_name.title()}.  Would you like to learn some {lang.title()} today?"
print(message)
print(full_name.upper())
print(full_name.lower())
print(full_name.title())
famous_person = 'mark twain'
quotation = ""
message = f"{famous_person.title()} once said"
quotation = "'Everyone complains about the weather, but nobody does anything about it!'"
myTuple = (message, quotation)
myTuple = " ".join(myTuple)
print(myTuple)
