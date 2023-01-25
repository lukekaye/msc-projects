'''
File holds Inventory class
'''
from item import Item
from stock import Stock
import os
import time

class Inventory(Stock):
    '''
    Class to create Inventory object composed of Item objects, with utilisation of csv database
    '''
    def __init__(self):
        '''
        Constructor that creates Inventory object by reading from a csv file, generates a blank csv if no file is found
        '''
        self.__stock = []
        # create database.csv if not found
        if not os.path.isfile('database.csv'):
            with open('database.csv', 'w'):
                pass
        # generate inventory object from database.csv
        with open('database.csv', 'r') as f:
            for i in f:
                line = i.strip().split(',')
                #  True, False text must manually be converted to boolean
                if line[2] == 'True':
                    line[2] = True
                elif line[2] == 'False':
                    line[2] = False
                self.__stock.append(Item(str(line[0]), str(line[1]), line[2], int(line[3]), float(line[4])))

    @property
    def stock(self):
        '''
        Getter method for the Inventory object (i.e. the listing of stored items)
        '''
        return self.__stock

    def save_and_quit(self):
        '''
        Method to save internally loaded state of stock system to csv file and then quit program
        '''
        with open('database.csv', 'w') as f:
            for i in range(len(self.stock)):
                # convert sell_price of item to int if item has no decimal places, removes redundant decimal place 0s
                if str(self.stock[i].sell_price).split('.')[1] == '0':
                    self.stock[i].sell_price = int(self.stock[i].sell_price)
                # save stock system to csv file
                f.write(','.join(
                    [str(self.stock[i].name), str(self.stock[i].category), str(self.stock[i].perishable),
                     str(self.stock[i].stock), str(self.stock[i].sell_price)]))
                f.write('\n')
        print('\nSaved successfully, program will terminate in 5s')
        time.sleep(5) # wait for 5 seconds
        raise SystemExit # quits the program