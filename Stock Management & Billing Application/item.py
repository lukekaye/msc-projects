'''
File holds Item class
'''
class Item:
    '''
    Class to create item objects through use of the inventory class
    '''
    def __init__(self, name, category, perishable, stock, sell_price):
        '''
        Constructor that instantiates item objects with private instance variables of appropriate type
        '''
        # check for correct variable types
        if not isinstance(name, str) or not isinstance(category, str) or not isinstance(perishable, bool) \
                or not isinstance(stock, int) or not isinstance(sell_price, float) \
                or len(str(sell_price).split('.')[1]) > 2 or stock < 0 or sell_price < 0:
            raise TypeError()
        # upon passing type checks, define variables
        self.__name = name.lower()
        self.__category = category.lower()
        self.__perishable = perishable
        self.__stock = stock
        self.__sell_price = sell_price

    def __str__(self):
        '''
        String representation of an item
        '''
        return f'Name: {self.name} | Category: {self.category} | Perishable: ' \
               f'{self.perishable} | Stock: {self.stock} | Sell Price: £{self.sell_price:.2f}'

    def __repr__(self):
        '''
        Formal string representation of an item
        '''
        return f'Item({self.name}, {self.category}, {self.perishable}, {self.stock}, {self.sell_price})'

    # Block of getter methods for private instance variables
    @property
    def name(self):
        return self.__name

    @property
    def category(self):
        return self.__category

    @property
    def perishable(self):
        return self.__perishable

    @property
    def stock(self):
        return self.__stock

    @property
    def sell_price(self):
        return self.__sell_price

    # Block of setter methods for private instance variables
    @name.setter
    def name(self, name):
        self.__name = name

    @category.setter
    def category(self, category):
        self.__category = category

    @perishable.setter
    def perishable(self, perishable):
        self.__perishable = perishable

    @stock.setter
    def stock(self, stock):
        self.__stock = stock

    @sell_price.setter
    def sell_price(self, sell_price):
        self.__sell_price = sell_price