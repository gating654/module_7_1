from pprint import pprint


class Product:
    def __init__(self, name, weight: float, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop():
    __file_name = 'products.txt'
    fr = open(__file_name, "r")
    fw = open(__file_name, "w")

    def get_products(self):
        pprint(self.fr.read())
        self.fr.close()
        return

    def add(self, *products):
        for product in products:
            if product.name not in self.get_products():
                self.fw.write(str(product))
                self.fw.write('\n')
            else:
                print(f"Продукт, '{product.name}' уже есть в магазине.")
            return
        self.fw.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())
