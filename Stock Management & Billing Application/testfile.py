'''
File holds all unit testing methods, note that only class functionality is tested here, not main script functionality
Note that running this testfile will replace the database.csv file with a sample one used for testing purposes
The previous database.csv file will be saved temporarily within this running script to then be restored after testing
Aborting this script while it is running, i.e. before completion, may prevent the user database file from being restored

All unit testing is done here, each test suite is self-contained in its own class
Each test suite is aimed at a different part of the specification
Before each test suite, the sample database.csv is generated using setUp methods
'''
from item import Item
from stock import Stock
from inventory import Inventory
from basket import Basket
import unittest

# contents of sample database.csv for testing
database_default = 'gold ring,jewellery,False,4,180\n' \
                   'jade bracelet,jewellery,False,2,250\n' \
                   'tt handmade shell necklace,jewellery,False,15,90\n' \
                   'tt homemade strawberry jam,food,True,30,6\n' \
                   'tt homemade blackberry jam,food,True,20,6\n' \
                   'tt homemade shortbread,food,True,10,8\n' \
                   'local postcard,misc,False,50,3\n' \
                   'handwoven basket,home,False,15,15\n' \
                   'village canvas,home,False,10,150\n' \
                   'small animal sculpture,home,False,5,25\n'

# saving of user database.csv to later be restored
with open('database.csv', 'r') as f:
    database_custom = f.read()

# note that most tests that apply to Stock derived sub class objects are performed on Inventory objects
# this is because Inventory objects instantiate with a sample set of items from the test database.csv

# Basket and Inventory objects are similar enough that replicating these unit tests on Basket objects would--
# largely be redundant. a few specific cases are interesting enough to be worth doing, and can be found occasionally

class TestGeneral(unittest.TestCase):
    '''
    General tests that don't directly fit any part of the specification
    '''
    def test_general(self):
        test_item = Item('AAA', 'BBB', True, 1, 2.5) # instantiate test_item
        self.assertIsInstance(test_item, Item) # check test_item is Item object
        # check string representations of test_item, also implicitly checks getter methods
        self.assertEqual(test_item.__str__(), \
                         'Name: aaa | Category: bbb | Perishable: True | Stock: 1 | Sell Price: £2.50')
        self.assertEqual(test_item.__repr__(), 'Item(aaa, bbb, True, 1, 2.5)')
        test_inventory1 = Inventory() # instantiate test_inventory1
        test_inventory2 = Inventory() # instantiate test_inventory2
        # test __eq__ method, test_inventory1 and test_inventory2 are both identical so this should hold
        self.assertEqual(test_inventory1, test_inventory2)
        # modify test_inventory2 so it is different to test_inventory1
        test_inventory2.stock.append(Item('test_name', 'test_category', True, 999, 999.99))
        # test __eq__ method, test_inventory1 and test_inventory2 are no longer identical so this should hold
        self.assertNotEqual(test_inventory1, test_inventory2)

    def test_general_errors(self):
        # error case tests for incorrect variable types when instantiating item objects
        with self.assertRaises(TypeError):
            Item(1, 'b', True, 1, 2.5)
        with self.assertRaises(TypeError):
            Item('a', 1, True, 1, 2.5)
        with self.assertRaises(TypeError):
            Item('a', 'b', 'True', 1, 2.5)
        with self.assertRaises(TypeError):
            Item('a', 'b', True, 0.1, 2.5)
        with self.assertRaises(TypeError):
            Item('a', 'b', True, 1, '2.5')
        with self.assertRaises(TypeError):
            Item('a', 'b', True, 1, 2.501)
        with self.assertRaises(TypeError):
            Item('a', 'b', True, -1, 2.5)
        with self.assertRaises(TypeError):
            Item('a', 'b', True, 1, -2.5)
        # test that a Stock object can't be instantiated due to abstractness
        with self.assertRaises(TypeError):
            Stock()

class TestRetrieveSave(unittest.TestCase):
    '''
    Tests applicable to retrieving and saving stock information via csv file
    '''
    def setUp(self): # generate sample database.csv file in most test classes
        with open('database.csv', 'w') as f:
            f.write(database_default)

    def test_retrieve_save(self):
        test_inventory = Inventory() # instantiate test_inventory
        self.assertIsInstance(test_inventory, Inventory) # check test_inventory is Inventory object
        for i in range(len(test_inventory.stock)): # check elements of test_inventory are type Item
            self.assertIsInstance(test_inventory.stock[i], Item)
        with self.assertRaises(SystemExit): # check save_and_quit method runs fully and exits program successfully
            test_inventory.save_and_quit()

    # restore user database.csv file in most test classes
    # has to be placed in every class with a sample database setUp method due to unpredictability of unittest library
    def tearDown(self):
        with open('database.csv', 'w') as f:
            f.write(database_custom)

class TestSearch(unittest.TestCase):
    '''
    Tests applicable to returning entries from the database of stock items
    '''
    def setUp(self):
        with open('database.csv', 'w') as f:
            f.write(database_default)

    def test_search(self):
        test_inventory = Inventory() # instantiate test_inventory
        # for some of these tests, to save space, only a portion of the total output is checked for validity
        # check string representations of test_inventory, also implicitly checks getter method
        self.assertEqual(test_inventory.__str__()[0:185], 'Name: gold ring | Category: jewellery | Perishable: False | '
                                                          'Stock: 4 | Sell Price: £180.00\nName: jade bracelet | '
                                                          'Category: jewellery | Perishable: False | Stock: 2 | '
                                                          'Sell Price: £250.00')
        self.assertEqual(test_inventory.__repr__()[0:91], 'Item(gold ring, jewellery, False, 4, 180.0)\n'
                                                          'Item(jade bracelet, jewellery, False, 2, 250.0)')
        # success case tests for search_stock method string return
        self.assertEqual(test_inventory.search_stock('*', '')[0],test_inventory.__str__())
        self.assertEqual(test_inventory.search_stock('invalid', 'invalid')[0],
                         'No items were found satisfying these conditions')
        self.assertEqual(test_inventory.search_stock('name', 'gold ring')[0], 'Name: gold ring | '
                                                                                  'Category: jewellery | '
                                                                                  'Perishable: False | Stock: 4 | '
                                                                                  'Sell Price: £180.00')
        self.assertEqual(test_inventory.search_stock('category', 'misc')[0], 'Name: local postcard | '
                                                                                 'Category: misc | Perishable: False | '
                                                                                 'Stock: 50 | Sell Price: £3.00')
        self.assertEqual(test_inventory.search_stock('perishable', False)[0][0:185],'Name: gold ring | Category: '
                                                                                       'jewellery | Perishable: False'
                                                                                       ' | Stock: 4 | Sell Price:'
                                                                                       ' £180.00\nName: jade bracelet'
                                                                                       ' | Category: jewellery |'
                                                                                       ' Perishable: False | '
                                                                                       'Stock: 2 | Sell Price: £250.00')
        self.assertEqual(test_inventory.search_stock('price', 6.0)[0], 'Name: tt homemade strawberry jam | '
                                                                        'Category: food | Perishable: True | '
                                                                        'Stock: 30 | Sell Price: £6.00\n'
                                                                        'Name: tt homemade blackberry jam | '
                                                                        'Category: food | Perishable: True | '
                                                                        'Stock: 20 | Sell Price: £6.00')
        # tests for empty and nonempty flags in search_stock return
        self.assertEqual(test_inventory.search_stock('price', 99999)[1], 0) # empty flag test
        self.assertEqual(test_inventory.search_stock('name', 'gold ring')[1], 1) # nonempty flag test
        # no error case tests here are applicable due to how main.py parses user inputs for passing to search_stock

    def tearDown(self):
        with open('database.csv', 'w') as f:
            f.write(database_custom)

class TestAdd(unittest.TestCase):
    '''
    Tests applicable to adding Item entries to Inventory
    '''
    def setUp(self):
        with open('database.csv', 'w') as f:
            f.write(database_default)

    def test_add(self):
        test_inventory1 = Inventory() # instantiate test_inventory1, will have add_item method applied to it
        test_inventory2 = Inventory() # instantiate test_inventory2, will not be modified
        # test that something is added to the inventory object
        test_inventory1.add_item('a name', 'a category', True, 999, 999.99)
        self.assertNotEqual(test_inventory1,test_inventory2)
        # test that the 'something' is indeed an Item object, by definition add_item places the new Item at the end
        self.assertIsInstance(test_inventory1.stock[-1], Item)
        # no need to test for incorrect parameter types or duplicate names as the main loop prevents this

    def tearDown(self):
        with open('database.csv', 'w') as f:
            f.write(database_custom)

class TestEdit(unittest.TestCase):
    '''
    Tests applicable to editing Item entries within Inventory
    '''
    def setUp(self):
        with open('database.csv', 'w') as f:
            f.write(database_default)

    def test_edit(self):
        test_inventory1 = Inventory() # instantiate test_inventory1, will have edit_item method applied to it
        test_inventory2 = Inventory() # instantiate test_inventory2, will not be modified
        # test that editing does not occur when no item is found, only needs to be tested for name parameter
        test_inventory1.edit_item('name', 'nonexistent item', 'different name')
        self.assertEqual(test_inventory1, test_inventory2) # uses __eq__ Inventory method
        # block of tests to test that editing does not occur when proposed value is identical to previous value
        test_inventory1.edit_item('category', 'gold ring', 'jewellery') # attempt category edit
        self.assertEqual(test_inventory1, test_inventory2)
        self.assertEqual(test_inventory1.edit_item('category', 'gold ring', 'jewellery'), 0) # 0 flag means no change
        test_inventory1.edit_item('perishable', 'gold ring', False) # attempt perishable edit
        self.assertEqual(test_inventory1, test_inventory2)
        self.assertEqual(test_inventory1.edit_item('perishable', 'gold ring', False), 0)
        test_inventory1.edit_item('stock', 'gold ring', 4) # attempt stock edit
        self.assertEqual(test_inventory1, test_inventory2)
        self.assertEqual(test_inventory1.edit_item('stock', 'gold ring', 4), 0)
        test_inventory1.edit_item('price', 'gold ring', 180) # attempt price edit
        self.assertEqual(test_inventory1, test_inventory2)
        self.assertEqual(test_inventory1.edit_item('price', 'gold ring', 180), 0)
        # instantiate more test_inventory objects, each will have one parameter tested for changes and flag returns
        test_inventory3 = Inventory()
        test_inventory4 = Inventory()
        test_inventory5 = Inventory()
        test_inventory6 = Inventory()
        # block of tests to test that editing occurs when appropriate parameters are passed
        test_inventory1.edit_item('name', 'gold ring', 'different name')
        test_inventory3.edit_item('category', 'gold ring', 'different category')
        test_inventory4.edit_item('perishable', 'gold ring', True)
        test_inventory5.edit_item('stock', 'gold ring', 9999)
        test_inventory6.edit_item('price', 'gold ring', 9999)
        self.assertNotEqual(test_inventory1, test_inventory2) # equality tests
        self.assertNotEqual(test_inventory3, test_inventory2)
        self.assertNotEqual(test_inventory4, test_inventory2)
        self.assertNotEqual(test_inventory5, test_inventory2)
        self.assertNotEqual(test_inventory6, test_inventory2)
        self.assertEqual(test_inventory1.edit_item('name', 'jade bracelet', 'different name'), 1) # 1 flag means change
        self.assertEqual(test_inventory3.edit_item('category', 'jade bracelet', 'different category'), 1)
        self.assertEqual(test_inventory4.edit_item('perishable', 'jade bracelet', True), 1)
        self.assertEqual(test_inventory5.edit_item('stock', 'jade bracelet', 9999), 1)
        self.assertEqual(test_inventory6.edit_item('price', 'jade bracelet', 9999), 1)

    def tearDown(self):
        with open('database.csv', 'w') as f:
            f.write(database_custom)

class TestDelete(unittest.TestCase):
    '''
    Tests applicable to deleting Item entries from Inventory
    '''
    def setUp(self):
        with open('database.csv', 'w') as f:
            f.write(database_default)

    def test_delete(self):
        test_inventory1 = Inventory() # instantiate test_inventory1, will have delete_item method applied to it
        test_inventory2 = Inventory() # instantiate test_inventory2, will not be modified
        # test that deletion does not occur when no item is found
        test_inventory1.delete_item('nonexistent item')
        self.assertEqual(test_inventory1, test_inventory2) # uses __eq__ Inventory method
        # test that deletion works for valid inputs
        test_inventory1.delete_item('gold ring')
        self.assertNotEqual(test_inventory1, test_inventory2)

    def tearDown(self):
        with open('database.csv', 'w') as f:
            f.write(database_custom)

class TestPurchaseReceipt(unittest.TestCase):
    '''
    Tests applicable to 'purchasing' stock and generating receipts in the program
    '''
    def setUp(self):
        with open('database.csv', 'w') as f:
            f.write(database_default)

    def test_purchase_receipt(self):
        test_basket = Basket() # instantiate test_basket
        self.assertIsInstance(test_basket, Basket) # check test_basket is Basket object
        self.assertEqual(test_basket.__str__(), '') # check test_basket instantiates empty, implicitly checks getter
        test_inventory = Inventory() # instantiate test inventory
        # check quantity of gold ring, stating intent to purchase 2
        self.assertEqual(test_inventory.check_quantity('gold ring', 2), (4, 2)) # return stock = 4 and request <= stock
        # check quantity of gold ring, stating intent to purchase 5
        self.assertEqual(test_inventory.check_quantity('gold ring', 5), (4, 1)) # return stock = 4 and request > stock
        test_inventory.edit_item('stock', 'gold ring', 0) # set gold ring stock to 0
        # check quantity of gold ring, stating intent to purchase 1
        self.assertEqual(test_inventory.check_quantity('gold ring', 1), (0, 0)) # return stock = 0 with flag stock = 0
        # check correct parameters are returned when checking parameters of jade bracelet
        self.assertEqual(test_inventory.get_item_params('jade bracelet'), ('jade bracelet', 'jewellery', False, 2, 250))
        # functionality of Basket.checkout can be checked by manually deleting receipts folder and generating receipts

    def tearDown(self):
        with open('database.csv', 'w') as f:
            f.write(database_custom)

if __name__ == '__main__':
    unittest.main()