from product import Product

class Store(object):
    def __init__(self, id, name, location, owner):
        self.products = []
        self.id = id
        self.name = name
        self.location = location
        self.owner = owner
        print '~~~ Created new store {} ~~~'.format(name)
        self.info()

    def add_product(self, prodId, prodPrice, prodName, prodWeight, prodBrand, prodStatus="for sale"):
        print '~~~ Add Product to {} Store ~~~'.format(self.name)
        self.products.append(Product(prodId, prodPrice, prodName, prodWeight, prodBrand, prodStatus))
        return self

    def remove_product(self, prodName):
        removed = False
        for idx, product in enumerate(self.products):
            # if product exist in list
            if product.name == prodName:
                print "~~~ Removed Product {} from {}'s Inventory ~~~".format(prodName, self.name)
                self.products.pop(idx).display_info()
                removed = True
                break

        if not removed:
            print "~~~ Could not find Product {} in {}'s Inventory ~~~\n".format(prodName, self.name)

        return self
    
    def info(self):
        print "Store ID: {}\nStore Name: {}\nStore Location: {}\nStore Owner: {}".format(self.id, self.name, self.location, self.owner)
        return self

    def inventory(self):
        print "~~~ Display all Inventory for the {} Store ~~~\n".format(self.name)
        for product in self.products:
            product.display_info()

        return self

if(__name__ == "__main__"):
    print '~~~ Running from Store main ~~~\n'
    happyTime = Store(1, 'Happy Time Candy', 'Bellevue, WA', 'Willy Wonka')

    happyTime.add_product(1, 1000000.00, 'Everlasting Gobstopper', 0.5, 'Willy Wonka', 'not for sale')
    happyTime.add_product(2, 1.00, 'Triple Cream Cup', 0.75, 'Willy Wonka')
    happyTime.add_product(3, 2.00, 'Squelchy Snorter', 1.0, 'Willy Wonka')
    happyTime.add_product(4, 2.50, "Slugworth's Sizzler", 0.25, 'Willy Wonka')

    happyTime.remove_product('Squelchy Srter')
    happyTime.remove_product('Squelchy Snorter')

    happyTime.inventory()
else:
    print '~~~ Imported {} ~~~\n'.format(__name__)