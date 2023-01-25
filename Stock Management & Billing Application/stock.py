'''
File holds Stock abstract class, builds the framework of Inventory and Basket classes
'''
from abc import ABC, abstractmethod
from item import Item

class Stock(ABC):
    '''
    Class to provide common methods between Inventory and Basket objects
    '''
    def __str__(self):
        '''
        String representation of a Stock object
        '''
        # Returns a newline separated listing of item string representations
        stock_str = []
        for i in self.stock:
            stock_str.append(i.__str__())
        return '\n'.join(stock_str)

    def __repr__(self):
        '''
        Formal string representation of a Stock object
        '''
        # Returns a newline separated listing of item formal string representations
        stock_repr = []
        for i in self.stock:
            stock_repr.append(i.__repr__())
        return '\n'.join(stock_repr)

    def __eq__(self, other):
        '''
        Identity comparison for a Stock object
        '''
        # define two Stock objects to be identical if their representations match
        return self.__repr__() == other.__repr__()

    @property
    @abstractmethod
    def stock(self):
        '''
        Abstract getter method for Stock objects (i.e. the listing of stored items)
        '''
        pass

    def search_stock(self, choice, search):
        '''
        Method to search Stock object for Item objects container within
        '''
        # appends Item object __str__ representations to list based on choice and search variables
        searched_inventory = []
        if choice == '*': # if we're searching for all stock items
            for i in self.stock:
                searched_inventory.append(i.__str__())
        elif choice == 'name': # if we're searching for a given name of a stock item
            for i in self.stock:
                if i.name == search:
                    searched_inventory.append(i.__str__())
        elif choice == 'category': # if we're searching for a given category of stock items
            for i in self.stock:
                if i.category == search:
                    searched_inventory.append(i.__str__())
        elif choice == 'perishable': # if we're searching for a given perishable boolean of stock items
            for i in self.stock:
                if i.perishable == search:
                    searched_inventory.append(i.__str__())
        elif choice == 'price': # if we're searching for a given sell_price of stock items
            for i in self.stock:
                if i.sell_price == search:
                    searched_inventory.append(i.__str__())
        if len(searched_inventory) == 0: # check if no matches were found
            # returns tuple, first entry is information string, second is a flag stating that nothing was found
            return ('No items were found satisfying these conditions', 0)
        # returns tuple, first entry is information string, second is a flag stating that something was found
        return ('\n'.join(searched_inventory), 1) # newline separated listing of Item string representations

    def add_item(self, name, category, perishable, stock, price):
        '''
        Method to append an Item object within a Stock object
        '''
        # append an Item object with given parameters to a Stock object, which is itself a list of Items
        self.stock.append(Item(name, category, perishable, stock, price))

    def edit_item(self, choice, search, change):
        '''
        Method to edit a parameter of an Item object within a Stock object
        '''
        for i in self.stock: # search through stock object and find item to amend
            if i.name == search: # only amends the object with matching name specified previously
                if choice == 'name':
                    i.name = change # name is always changed here due to uniqueness so 1 is always returned
                    return 1
                elif choice == 'category':
                    if i.category == change:
                        # returns a flag if the category value was not changed, i.e. it was identical to the input
                        return 0
                    i.category = change
                    # returns a flag if the category value was changed, i.e. it was different to the input
                    return 1
                elif choice == 'perishable':
                    if i.perishable == change:
                        return 0 # flag return as described above, repeated for all parameters below
                    i.perishable = change
                    return 1
                elif choice == 'stock':
                    if i.stock == change:
                        return 0
                    i.stock = change
                    return 1
                elif choice == 'price':
                    if i.sell_price == change:
                        return 0
                    i.sell_price = change
                    return 1

    def delete_item(self, search):
        '''
        Method to delete an Item object within a Stock object
        '''
        for i in self.stock: # search through stock object and find item to be deleted
            if i.name == search:
                self.stock.remove(i) # delete the matched item object from the stock object

    def check_quantity(self, search, quantity):
        '''
        Method to check the current stock count of a given Item, defined by its name
        '''
        for i in self.stock: # search through inventory object and find item for adding to basket
            if i.name == search: # if the currently iterated item matches the search
                # returns a tuple with the stock count of the item and a flag
                if i.stock == 0:
                    return (i.stock, 0) # flag stating no available stock to purchase
                elif i.stock < quantity:
                    return (i.stock, 1) # flag stating user request exceeds available
                return (i.stock, 2) # flag stating no special condition

    def get_item_params(self, search):
        '''
        Method to get the value of all parameters for an Item in a Stock object, given its unique name
        '''
        for i in self.stock: # search through Stock object and find item
            if i.name == search: # if the currently iterated item matches the search
                return (i.name, i.category, i.perishable, i.stock, i.sell_price) # tuple with all parameters