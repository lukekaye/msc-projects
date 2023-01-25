'''
File holds Basket class
'''
from stock import Stock
import datetime
import os

class Basket(Stock):
    '''
    Class to create Basket object, which is populated with Item objects through user input in main program
    '''
    def __init__(self):
        '''
        Constructor that creates Basket object, begins as an empty list
        '''
        self.__stock = []

    @property
    def stock(self):
        '''
        Getter method for the Basket object (i.e. the listing of stored items)
        '''
        return self.__stock

    def checkout(self, member):
        '''
        Method to check out Items in Basket, with receipt generation
        '''
        receipt = [] # initialise blank receipt (list)
        total_cost = float(0) # initialise total cost (float)
        for i in enumerate(self.stock): # iterate through contents of Basket, each Item has an index through enumerate
            # append a list object to the receipt list with purchase count, item name, unit price, total cost for item
            receipt.append([i[1].stock, i[1].name, i[1].sell_price, i[1].sell_price * i[1].stock])
            total_cost += receipt[i[0]][3] # adds total cost for Item i to total cost for receipt
        # calculate member discount
        if member == True:
            # the specification specifically states 'if they spend MORE than £50' not MORE OR EQUAL to £50
            if total_cost > 50:
                discount = 0.9 # 10% discount
            else:
                discount = 0.95 # 5% discount
        elif member == False:
            discount = 1 # no discount
        discount_applied = round((1 - discount) * total_cost, 2) # calculate discount applied to total
        final_cost = round(total_cost * discount, 2) # calculate post discount total, rounded to 2 decimal places
        receipt_datetime = datetime.datetime.today().replace(microsecond=0) # get time of receipt generation
        # text based receipt
        # 10 chars for quantity, 30 chars for Item, 10 chars for Price and 20 chars for total
        print(f'\n-------------------------------------------------------------------------'
              f'\nPurchase Receipt                                      {receipt_datetime}'
              f'\n-------------------------------------------------------------------------'
              f'\nQuantity   Item                           Price      Total               ')
        for i in receipt:
            print(f'{i[0]: <10} {i[1]: <30} £{i[2]: <9.2f} £{i[3]: <19.2f}')
        print(f'-------------------------------------------------------------------------\n'
              f'Subtotal   £{total_cost: <61.2f}\n'
              f'Discount   £{discount_applied: <61.2f}\n'
              f'Total      £{final_cost: <61.2f}\n'
              f'-------------------------------------------------------------------------')
        # save receipt as txt file
        # first check if receipts folder exists, create it if not
        if not os.path.exists('receipts'):
            os.makedirs('receipts')
        # find first available index for receipt to be generated
        index = 1
        while True:
            path = f'./receipts/receipt ({index}).txt' # path of receipts folder
            # check receipts folder
            if os.path.isfile(path):  # if a receipt with the given index exists
                index += 1  # add 1 to index to then check the next receipt number
            else:
                break  # if no receipt is found with this index, this index will be that for the new receipt
        # now save the receipt
        receipt_file = os.path.join('./receipts', f'receipt ({index}).txt')
        with open (receipt_file, 'w') as f: # similar but not quite identical set of strings to the above
            f.write(f'-------------------------------------------------------------------------'
                      f'\nPurchase Receipt                                      {receipt_datetime}'
                      f'\n-------------------------------------------------------------------------'
                      f'\nQuantity   Item                           Price      Total               ')
            for i in receipt:
                f.write(f'\n{i[0]: <10} {i[1]: <30} £{i[2]: <9.2f} £{i[3]: <19.2f}')
            f.write(f'\n-------------------------------------------------------------------------\n'
                  f'Subtotal   £{total_cost: <61.2f}\n'
                  f'Discount   £{discount_applied: <61.2f}\n'
                  f'Total      £{final_cost: <61.2f}\n'
                  f'-------------------------------------------------------------------------')
        # receipt has now been saved to receipts directory
        print(f'\nreceipt ({index}) saved to receipts folder')