from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'product.txt'

    def get_products(self):
        file = open(Shop.__file_name, 'r')
        a = file.read()
        file.close()
        return a

    def add(self, *products):
        for i in range(len(products)):
            prod = str(products[i])
            if prod in str(Shop.get_products(self)):
                print(f'Продукт {prod} уже есть в магазине')
            else:
                file = open(Shop.__file_name, 'a')
                file.write(f'{prod}\n')
                file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
