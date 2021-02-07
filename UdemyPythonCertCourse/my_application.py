from Utils.utility_stuff import ListAndCharShortener, DictionaryShortener

myShortener = DictionaryShortener({1: 'mike', 2: 'tom', 3: 'marilyn', 4: 'mike', 5: 'paul'})
myShortener.print_shortened_items()
myShortener.print_original_items()


'''
myshortener = ListAndCharShortener("this is a sentence")
myshortener.print_shortened_items()
myshortener.print_original_items()
myshortener2 = ListAndCharShortener([1, 2, 3, 4, 5, 6])
myshortener2.print_shortened_items()
'''
