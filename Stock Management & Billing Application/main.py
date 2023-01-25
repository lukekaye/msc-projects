'''
Main file that program is initialised from, contains functionality for the menu of the program and user interactivity
'''

from item import Item
from inventory import Inventory
from basket import Basket

def checkout(bask):
    '''
    Function to facilitate checking out of Basket Items, with receipt generation
    '''
    contents = bask.search_stock('*', '')[0] # return contents of basket
    print(f'\nContents of basket:\n{contents}\n\nDo you wish to checkout these items? (y/n)')
    # try/except loop to ensure valid input
    while True:
        try:
            decision = input('\nSpecify decision: ').lower()  # specify yes or no
            # enforce valid input
            if not decision == 'y' and not decision == 'n':
                raise Exception
            break
        except Exception:
            print('Invalid input, enter "y", "n"')
    if decision == 'y':  # access checkout method here
        print(f'\nIs the customer purchasing these items a member? (y/n)')
        # specify if customer is a member
        # try/except loop to ensure valid input
        while True:
            try:
                member = input('\nSpecify decision: ').lower()  # specify yes or no
                # enforce valid input
                if not member == 'y' and not member == 'n':
                    raise Exception
                break
            except Exception:
                print('Invalid input, enter "y", "n"')
        # change member flag to boolean
        if member == 'y':
            member = True
        elif member == 'n':
            member = False
        bask.checkout(member) # access Basket method to generate receipt
        # now delete the contents of the basket in its entirety
        while not bask.stock == []: # check if basket is empty yet
            bask.delete_item(bask.stock[0].name) # delete the first item in the basket
    elif decision == 'n':  # return to main loop
        print(f'\nBasket was not checked out')
    # return to main loop after checkout decision

def add_to_basket(inv, bask):
    '''
    Function to allow the user to move items from the inventory object to the basket object for eventual checkout
    '''
    print('\nEnter the name of the item within the inventory you wish to add to the basket')
    search = input('\nSpecify name: ').lower() # user specifies name parameter corresponding to item they wish to add
    print('')
    result = inv.search_stock('name', search) # accesses search_stock to return information on user input
    print(result[0])
    if result[1] == 1: # if an item was found
        quantity_flag = inv.check_quantity(search, 0) # check stock of item, 2nd parameter is not important here
        if quantity_flag[1] == 0: # do nothing further if stock count for specified item is 0
            print(f'\n{search} has no available stock to purchase, therefore {search} was not added to basket')
        else:
            print(f'\nState quantity of {search} to add to basket')
            # try/except loop to ensure valid input
            while True:
                try:
                    quantity = input('\nSpecify quantity: ')
                    # enforce valid input
                    quantity = int(quantity) # check if input is an integer, and switch to correct type
                    if quantity < 0: # check if user input is non-negative
                        raise Exception
                    break
                except Exception:
                    print('Invalid input, enter a non-negative integer')
            if quantity == 0: # do nothing further if user specifies to add 0 to basket
                print(f'\n{search} was not added to basket')
            else: # if quantity > 0, continue this line of functionality
                quantity_flag = inv.check_quantity(search, quantity) # check quantity again, this time with user request
                if quantity_flag[1] == 1: # if user requested to purchase more than the available stock
                    print(f'\nAvailable stock of {search} ({quantity_flag[0]}) is less than requested amount'
                          f'\nPurchase maximum amount ({quantity_flag[0]}) instead? (y/n)')
                    while True: # user specifies yes or no to the above question
                        try:
                            decision = input('\nSpecify decision: ').lower()  # specify yes or no
                            # enforce valid input
                            if not decision == 'y' and not decision == 'n':
                                raise Exception
                            break
                        except Exception:
                            print('Invalid input, enter "y", "n"')
                    if decision == 'n': # if user doesn't want to instead add the maximum, do nothing further
                        print(f'\n{search} was not added to basket')
                        complete_function = 0 # flag to break out of this function
                    else: # if user does want to add the maximum to basket, continue this functionality
                        quantity = quantity_flag[0]
                        complete_function = 1 # flag to finish this function
                elif quantity_flag[1] == 2:
                    complete_function = 1 # flag to finish this function
                if complete_function == 1: # method to append Item to Basket takes place here
                    params = inv.get_item_params(search) # get parameters of item to add to basket
                    inv.edit_item('stock', search, quantity_flag[0]-quantity) # subtract purchase quantity from stock
                    # either add a new entry to the basket or update a current one
                    # check if some quantity of item appended to basket is already there
                    exists = bask.search_stock('name', search)[1]
                    if exists == 0: # if the item to be added to basket doesn't already exist in there
                        bask.add_item(search, params[1], params[2], quantity, params[4])
                        print(f'\n{quantity}x {search} was added to basket, item total in basket is {quantity}')
                    else: # if the item to be added already exists in the basket in some quantity
                        basket_stock = bask.check_quantity(search, 0)[0] # check quantity, 2nd parameter is irrelevant
                        bask.edit_item('stock', search, basket_stock + quantity)
                        print(f'\n{quantity}x {search} was added to basket, item total in basket is'
                              f' {quantity + basket_stock}')
    # specify to add something else to the basket or return to menu
    print('\n1: Add a different item to the basket\n2: Return to main menu')
    # try/except loop to ensure valid input
    while True:
        try:
            decision = input('\nSpecify selection: ') # choose next action
            # enforce valid input
            if not decision == '1' and not decision == '2':
                raise Exception
            break
        except Exception:
            print('Invalid input, enter "1", "2"')
    if decision == '1': # access this function again, if decision == '2' then function exits
        add_to_basket(inv, bask)
    # return to select_basket_mode function

def remove_from_basket(inv, bask):
    '''
    Function to allow user to move items from basket object to inventory object
    '''
    if bask.search_stock('*','')[1] == 0: # if basket object contains no items
        print('\nBasket is currently empty')
    else:
        print('\nEnter the name of the item within the basket you wish to remove and return to the inventory')
        search = input('\nSpecify name: ').lower() # user specifies name of item they wish to remove
        print('')
        result = bask.search_stock('name', search) # accesses search_stock to return information on user input
        print(result[0])
        if result[1] == 1:  # if an item was found
            print(f'\nAre you sure you wish to remove {search} from the basket and return it to the inventory? (y/n)')
            # try/except loop to ensure valid input
            while True:
                try:
                    decision = input('\nSpecify decision: ').lower()  # specify yes or no
                    # enforce valid input
                    if not decision == 'y' and not decision == 'n':
                        raise Exception
                    break
                except Exception:
                    print('Invalid input, enter "y", "n"')
            if decision == 'y':  # access methods to remove item from basket and return to inventory
                params = bask.get_item_params(search) # get parameters of item being returned
                bask.delete_item(search) # first delete the item from the basket entirely
                exists = inv.search_stock('name',search)[1] # existence check of item in inventory
                if exists == 0: # if the item to be returned to the inventory doesn't already exist in there
                    # this would only happen if the user deleted the Item from the inventory after adding it to basket
                    inv.add_item(search, params[1], params[2], params[3], params[4])
                else: # if the item to be returned already exists in the inventory (as expected)
                    inventory_stock = inv.check_quantity(search, 0)[0] # check quantity, 2nd parameter is irrelevant
                    inv.edit_item('stock', search, inventory_stock + params[3]) # stock in inventory + stock in basket
                print(f'\n{search} x{params[3]} was removed from the basket and returned to the inventory')
            elif decision == 'n':  # pass over basket removal methods, prompt to user that no removal happened
                print(f'\n{search} was not removed from the basket')
        # specify to add something else to the basket or return to menu
        print('\n1: Remove a different item from basket\n2: Return to main menu')
        # try/except loop to ensure valid input
        while True:
            try:
                decision = input('\nSpecify selection: ')  # choose next action
                # enforce valid input
                if not decision == '1' and not decision == '2':
                    raise Exception
                break
            except Exception:
                print('Invalid input, enter "1", "2"')
        if decision == '1':  # access this function again, if decision == '2' then function exits
            remove_from_basket(inv, bask)
        # return to select_basket_mode function

def select_basket_mode(inv, bask):
    '''
    Function to allow user to access either add_to_basket or remove_from_basket preliminary functions, or view contents
    '''
    print('\n1: Add an item to the basket\n2: Remove an item from the basket\n3: View the contents of the basket')
    # try/except loop to ensure valid input
    while True:
        try:
            choice = input('\nSpecify selection: ') # choose basket edit type
            # enforce valid input
            if not choice == '1' and not choice == '2' and not choice == '3':
                raise Exception
            break
        except Exception:
            print('Invalid input, enter "1", "2", "3"')
    # choice dictates which function is accessed
    if choice == '1':
        add_to_basket(inv, bask)
    elif choice == '2':
        remove_from_basket(inv, bask)
    elif choice == '3':
        if bask.search_stock('*', '')[1] == 0: # if basket object contains no items
            print('\nBasket is currently empty')
        else: # else print basket contents
            print(f'\n{bask}')
    # eventually, after returning here from basket preliminary functions, return to menu function

def add_item_preliminary(inv):
    '''
    Function to allow user to specify parameter for accessing add_item Inventory class method
    '''
    print('\nEnter the name of the item you wish to add')
    # try/except loop to ensure valid input, proposed name cannot contain commas
    while True:
        try:
            prop_name = input('\nSpecify name: ').lower() # user specifies proposed name
            # enforce valid input
            if ',' in prop_name:
                raise Exception
            result = inv.search_stock('name', prop_name)  # accesses search_stock to return information
            break
        except Exception:
            print('Invalid input, proposed name cannot contain commas (",")')
    if result[1] == 1: # if an item was found
        print('\nAn item already exists with that name, with these parameters:')
        print(f'{result[0]}')
    elif result[1] == 0: # if no item was found
        # try/except loop to ensure valid input
        print(f'\nEnter the category for proposed item "{prop_name}"')
        prop_category = input('\nSpecify category: ').lower()  # user specifies category
        print(f'\nEnter the perishable condition for proposed item "{prop_name}"')
        while True:
            try:
                prop_perishable = input('\nSpecify perishable: ').lower() # user specifies perishable
                # enforce valid input
                if not prop_perishable == 'true' and not prop_perishable == 'false':
                    raise Exception
                break
            except Exception:
                print('Invalid input, enter "true", "false"')
        # change input to boolean format
        if prop_perishable == 'true':
            prop_perishable = True
        elif prop_perishable == 'false':
            prop_perishable = False
        print(f'\nEnter the stock for proposed item "{prop_name}"')
        while True:
            try:
                prop_stock = input('\nSpecify stock: ') # user specifies stock
                # enforce valid input
                prop_stock = int(prop_stock)  # check if user input is an integer, and switch to correct type
                if prop_stock < 0:  # check if user input is non-negative
                    raise Exception
                break
            except Exception:
                print('Invalid input, enter a non-negative integer')
        print(f'\nEnter the price for proposed item "{prop_name}"')
        while True:
            try:
                prop_price = input('\nSpecify stock: ') # user specifies price
                # enforce valid input
                prop_price = float(prop_price)  # check if user input is a float, and switch to correct type
                # check if user input has more than 2 decimal places or is non-negative
                if len(str(prop_price).split('.')[1]) > 2 or prop_price < 0:
                    raise Exception
                break
            except Exception:
                print('Invalid input, '
                      'enter a non-negative (rational) number of no more than 2 decimal places')
        # confirmation prompt for addition
        print(f'\nAre you sure you wish to add the the following item? (y/n):'
              f'\n{Item(prop_name, prop_category, prop_perishable, prop_stock, prop_price)}')
        # try/except loop to ensure valid input
        while True:
            try:
                decision = input('\nSpecify decision: ').lower() # specify yes or no
                # enforce valid input
                if not decision == 'y' and not decision == 'n':
                    raise Exception
                break
            except Exception:
                print('Invalid input, enter "y", "n"')
        if decision == 'y': # access add_item method here
            inv.add_item(prop_name, prop_category, prop_perishable, prop_stock, prop_price)
            print(f'\n{prop_name} was added')
        elif decision == 'n': # pass over add_item method, prompt to user to confirm no add happened
            print(f'\n{prop_name} was not added')
    print('\n1: Add another item\n2: Return to main menu') # specify to add something else or return to menu
    # try/except loop to ensure valid input
    while True:
        try:
            decision = input('\nSpecify selection: ') # choose next action
            # enforce valid input
            if not decision == '1' and not decision == '2':
                raise Exception
            break
        except Exception:
            print('Invalid input, enter "1", "2"')
    if decision == '1': # access this function again, if decision == '2' then function exits
        add_item_preliminary(inv)
    # return to select_modify_mode function

def edit_item_preliminary(inv):
    '''
    Function to allow user to specify parameter for accessing edit_item Inventory class method
    '''
    print('\nEnter the exact name of the item you wish to edit')
    search = input('\nSpecify name: ').lower() # user specifies name parameter corresponding to item they wish to edit
    result = inv.search_stock('name', search) # accesses search_stock to return information on user input
    print(f'\n{result[0]}')
    if result[1] == 1: # if an item was found
        print(f'\nSelect which parameter of {search} to edit ("name", "category", "perishable", "stock", "price")')
        # try/except loop to ensure valid input
        while True:
            try:
                choice = input('\nSpecify parameter: ').lower()  # choose item parameter to edit
                # enforce valid input
                if not choice == 'name' and not choice == 'category' and not choice == 'perishable' \
                        and not choice == 'stock' and not choice == 'price':
                    raise Exception
                break
            except Exception:
                print('Invalid input, enter "name", "category", "perishable", "stock", "price"')
        print(f'\nEnter value to change {choice} parameter of {search} to')
        # try/except loop to ensure valid input, valid input range will depend on selected parameter
        while True:
            try:
                change = input('\nSpecify value: ').lower() # choose value to change specified parameter to
                # first check if user input contains commas
                if ',' in change:
                    raise Exception
                # no check necessary for category
                if choice == 'name': # enforce valid input for name parameter
                    # search database for existing entries with name parameter equal to user input
                    compare = inv.search_stock('name', change)[1]
                    if compare == 1: # if an item was found with user specified replacement name
                        raise Exception
                elif choice == 'perishable': # enforce valid input for perishable parameter
                    if not change == 'true' and not change == 'false':
                        raise Exception
                elif choice == 'stock':
                    change = int(change) # check if user input is an integer, and switch to correct type
                    if change < 0: # check if user input is non-negative
                        raise Exception
                elif choice == 'price':
                    change = float(change) # check if user input is a float, and switch to correct type
                    # check if user input has more than 2 decimal places or is non-negative
                    if len(str(change).split('.')[1]) > 2 or change < 0:
                        raise Exception
                break
            except Exception: # error message dependent on parameter choice
                if ',' in str(change):
                    print('Invalid input, proposed value cannot contain commas (",")')
                elif choice == 'name':
                    print('Invalid input, an item with this name already exists')
                elif choice == 'perishable':
                    print('Invalid input, enter "true", "false"')
                elif choice == 'stock':
                    print('Invalid input, enter a non-negative integer')
                elif choice == 'price':
                    print('Invalid input, '
                          'enter a non-negative (rational) number of no more than 2 decimal places')
        # change format for perishable parameter from string to boolean
        if choice == 'perishable' and change == 'true':
            change = True
        elif choice == 'perishable' and change == 'false':
            change = False
        if choice == 'price': # confirmation prompt for price change
            print(f'\nAre you sure you wish to change the {choice} value of {search} to £{change:.2f}? (y/n)')
        else: # confirmation prompt for other parameter change
            print(f'\nAre you sure you wish to change the {choice} value of {search} to {change}? (y/n)')
        # try/except loop to ensure valid input
        while True:
            try:
                decision = input('\nSpecify decision: ').lower() # specify yes or no
                # enforce valid input
                if not decision == 'y' and not decision == 'n':
                    raise Exception
                break
            except Exception:
                print('Invalid input, enter "y", "n"')
        if decision == 'y': # access edit_item method here and store the returned flag as changed variable
            changed = inv.edit_item(choice, search, change)
            if changed == 0: # if a flag was returned stating the proposed value was identical to the current
                print(f'\n{search} {choice} value was not changed as proposed value was equal to its previous value')
            elif changed == 1: # if a flag was returned stating the proposed value was different to the current
                print(f'\n{search} {choice} value was changed to {change}')
        elif decision == 'n': # pass over edit_item method, prompt to user to confirm no edit happened
            print('')
            print(f'{search} {choice} value was not changed')
    print('\n1: Edit another item\n2: Return to main menu') # specify to edit something else or return to menu
    # try/except loop to ensure valid input
    while True:
        try:
            decision = input('\nSpecify selection: ') # choose next action
            # enforce valid input
            if not decision == '1' and not decision == '2':
                raise Exception
            break
        except Exception:
            print('Invalid input, enter "1", "2"')
    if decision == '1': # access this function again, if decision == '2' then function exits
        edit_item_preliminary(inv)
    # return to select_modify_mode function

def delete_item_preliminary(inv):
    '''
    Function to allow user to specify parameter for accessing delete_item Inventory class method
    '''
    print('\nEnter the exact name of the item you wish to delete')
    search = input('\nSpecify name: ').lower() # user specifies name parameter corresponding to item they wish to delete
    print('')
    result = inv.search_stock('name', search) # accesses search_stock to return information on user input
    print(result[0])
    if result[1] == 1: # if an item was found
        print(f'\nAre you sure you wish to delete {search}? (y/n)')
        # try/except loop to ensure valid input
        while True:
            try:
                decision = input('\nSpecify decision: ').lower() # specify yes or no
                # enforce valid input
                if not decision == 'y' and not decision == 'n':
                    raise Exception
                break
            except Exception:
                print('Invalid input, enter "y", "n"')
        if decision == 'y': # access delete_item method here
            inv.delete_item(search)
            print(f'\n{search} was deleted')
        elif decision == 'n': # pass over delete_item method, prompt to user to confirm no deletion happened
            print(f'\n{search} was not deleted')
    print('\n1: Delete another item\n2: Return to main menu') # specify to delete something else or return to menu
    # try/except loop to ensure valid input
    while True:
        try:
            decision = input('\nSpecify selection: ') # choose next action
            # enforce valid input
            if not decision == '1' and not decision == '2':
                raise Exception
            break
        except Exception:
            print('Invalid input, enter "1", "2"')
    if decision == '1': # access this function again, if decision == '2' then function exits
        delete_item_preliminary(inv)
    # return to select_modify_mode function

def select_modify_mode(inv):
    '''
    Function to allow user to choose which item modification main file preliminary function to access
    '''
    print('\n1: Add an item\n2: Edit an item\n3: Delete an item\n4: Return to main menu')
    # try/except loop to ensure valid input
    while True:
        try:
            choice = input('\nSpecify selection: ') # choose modification type
            # enforce valid input
            if not choice == '1' and not choice == '2' and not choice == '3' and not choice == '4':
                raise Exception
            break
        except Exception:
            print('Invalid input, enter "1", "2", "3", "4"')
    # choice variable dictates which preliminary function to access
    if choice == '1':
        add_item_preliminary(inv)
    elif choice == '2':
        edit_item_preliminary(inv)
    elif choice == '3':
        delete_item_preliminary(inv)
    # eventually, after returning here from add/edit/delete main file preliminary functions, return to menu function

def search(inv):
    '''
    Function to allow user to define parameters to access search_stock inherited Inventory class method
    '''
    print('\nChoose item parameter to search ("name", "category", "perishable", "price")\n'
          'Alternatively, enter "*" to display entire contents of database')
    # try/except loops are used here to ensure valid user inputs
    while True:
        try:
            choice = input('\nSpecify parameter: ').lower() # choose item parameter to search for
            # enforce valid input
            if not choice == '*' and not choice == 'name' and not choice == 'category' \
                    and not choice == 'perishable' and not choice == 'price':
                raise Exception
            if not choice == '*':
                while True:
                    try:
                        # obtain string to search for from user
                        search = input(f'\nSpecify search term for {choice}: ').lower()
                        # enforce valid input
                        # input check applicable to perishable only
                        if (choice == 'perishable' and not search == 'true') and \
                                (choice == 'perishable' and not search == 'false'):
                            raise Exception
                        # change price input to sell_price acceptable format and check validity
                        if choice == 'price':
                            search = float(search) # should correctly raise an exception if user input is invalid
                        # check if a price parameter search term has more than 2 decimal places or is negative
                        if (choice == 'price' and len(str(search).split('.')[1]) > 2) or \
                                (choice == 'price' and search < 0):
                            raise Exception
                        break
                    except Exception: # error message depends on parameter
                        if choice == 'perishable':
                            print('Invalid input, enter "true", "false"')
                        elif choice == 'price':
                            print('Invalid input, '
                                  'enter a non-negative (rational) number of no more than 2 decimal places')

            else: # if choice == '*', set search variable to blank string to allow passing to search_stock method
                search = ''
            break
        except Exception:
            print('Invalid input, enter "name", "category", perishable", "price", "*"')
    # perishable standardise to Item object perishable parameter format
    if choice == 'perishable' and search == 'true':
        search = True
    elif choice == 'perishable' and search == 'false':
        search = False
    print(f'\n{inv.search_stock(choice, search)[0]}') # access search_stock method for querying and print result
    # after running search_stock, returns to menu function

def menu(inv, bask):
    '''
    Program main menu, functionality is accessed through imported class methods
    '''
    # main menu, enclosed in try/except loop to ensure valid user inputs
    while True:
        try:
            print('\nSTOCK SYSTEM TOOL - Main Menu')
            print('\n1: Search for items\n2: Add/Edit/Delete items\n3: Edit/View shopping basket'
                  '\n4: Checkout basket and generate receipt\n5: Save changes and quit program')
            choice = input('\nSpecify function: ')
            if choice == '1': # search for items
                search(inv)
            elif choice == '2': # add/edit/delete items
                select_modify_mode(inv)
            elif choice =='3': # edit/view shopping basket
                select_basket_mode(inv, bask)
            elif choice == '4': # checkout basket and generate receipt
                if bask.search_stock('*', '')[1] == 0:  # if basket object contains no items
                    print('\nBasket is currently empty')
                else: # if basket does contain items
                    checkout(bask)
            elif choice == '5': # save changes and quit program
                # first check if basket contains Items
                basket_empty = bask.search_stock('*','')[1] # return empty condition flag from search_stock
                if basket_empty == 1: # if flag is returned from search_stock stating that basket is nonempty
                    # add contents of basket back to inventory, works similarly to remove_from_basket main loop function
                    for i in bask.stock: # iterate over entire Basket list
                        exists = inv.search_stock('name', i.name)[1] # check if iterated Basket Item exists in inventory
                        if exists == 0: # if the item to be returned to the inventory doesn't already exist in there
                            inv.add_item(i.name, i.category, i.perishable, i.stock, i.sell_price)
                        else: # if the item to be returned already exists in the inventory (as expected)
                            inventory_stock = inv.check_quantity(i.name, 0)[0] # check quantity, 2nd param irrelevant
                            inv.edit_item('stock', i.name, inventory_stock + i.stock)
                    # no need to delete Basket Items after returning them to Inventory
                inv.save_and_quit()
            else:
                raise Exception # any incorrect input prompts for a new input
        except Exception: # allows SystemExit exception to raise in save_and_quit method
            print('Invalid input, enter "1", "2", "3", "4", "5"')

def main():
    '''
    Program is initialised here
    '''
    inv = Inventory() # instantiate Inventory object, stored as inv
    bask = Basket() # instantiate Basket object, stored as bask
    menu(inv, bask)

if __name__ == '__main__':
    main()