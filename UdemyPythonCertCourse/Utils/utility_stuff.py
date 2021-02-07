class Shortener:
    def __init__(self, items):
        self.original_items = items
    
    def print_original_items(self):
        print(self.original_items)

class ListAndCharShortener(Shortener):
    def print_shortened_items(self):
        print(self.original_items[0:3])

class DictionaryShortener(Shortener):
    def print_shortened_items(self):
        dict         = self.original_items
        counter      = 0 
        result_dict  = {}
        for  (k,v) in dict.items():
            if (counter < 3):
                result_dict.update({k: v})
                counter += 1
        print(result_dict)

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
