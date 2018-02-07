from product import Product
from store import Store

storeId = 0
prodId = 0

def getStoreId():
    global storeId
    pStart = 1
    pInterval = 1
    if (storeId == 0):
        storeId = pStart
    else:
        storeId += pInterval
    return storeId

def getProdId():
    global prodId
    pStart = 1
    pInterval = 1
    if (prodId == 0):
        prodId = pStart
    else:
        prodId += pInterval
    return prodId

class Manage(object):
    def __init__(self):
        self.stores = []
        self.products = []

    def add_store(self, storeName, storeLoc, storeOwner):
        print '~~~ Add Store {} to Manager ~~~'.format(prodName)
        self.stores.append(Store(getStoreId(), storeName, storeLoc, storeOwner))
        return self

    def remove_store(self):
        print "~~~ Remove Store to Manager ~~~"
        return self

    def add_product(self, prodPrice, prodName, prodWeight, prodBrand, prodStatus="Warehouse"):
        print '~~~ Add Product {} to Manager ~~~'.format(prodName)
        self.products.append(Product(getProdId(), prodPrice, prodName, prodWeight, prodBrand, prodStatus))
        return self

    def remove_product(self, prodName):
        removed = False
        for idx, product in enumerate(self.products):
            # if product exist in list
            if product.name == prodName:
                print "~~~ Removed Product {} from Manager's Inventory ~~~".format(prodName)
                self.products.pop(idx).display_info()
                removed = True
                break

        if not removed:
            print "~~~ Could not find Product {} in Manager's Inventory ~~~\n".format(prodName)

        return self

    def send_item_to_store(self):
        print "~~~ Remove Product to Manager ~~~"
        return self

districtManager = Manage()

districtManager.add_product(1000000.00, 'Everlasting Gobstopper', 0.5, 'Willy Wonka', 'Out of Stock')
districtManager.add_product(1.00, 'Triple Cream Cup', 0.75, 'Willy Wonka')
districtManager.add_product(2.00, 'Squelchy Snorter', 1.0, 'Willy Wonka')
districtManager.add_product(2.50, "Slugworth's Sizzler", 0.25, 'Willy Wonka')

districtManager.add_store('Happy Time Candy', 'Bellevue, WA', 'Willy Wonka')
districtManager.add_store('Sappy Time Candy', 'Bellevue, WA', 'Willy Wonka')
districtManager.add_store('Slappy Time Candy', 'Bellevue, WA', 'Willy Wonka')
districtManager.add_store('Pappy Time Candy', 'Bellevue, WA', 'Willy Wonka')