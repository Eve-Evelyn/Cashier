def request_add_item(new_transaction):
    """Ask user to input the details of the new item they would like to add"""
    new_item_name = input("Input the name of item: ")

    while True:
        try:
            new_item_qty = int(input("Input the qty of item: "))
        except ValueError:
            print("Please enter an integer value only")
        else:
            break

    while True:
        try:
            new_item_price = int(input("Input the price of item: "))
        except ValueError:
            print("Please enter an integer value only")
        else:
            break

    new_transaction.add_item(new_item_name, new_item_qty, new_item_price)


def request_update_item(new_transaction, item_to_mod):
    """Ask user to input the details of the item they would like to update"""
    if item_to_mod not in new_transaction.item_name:
        print("\033[1m" + "\033[91m" + "Item not found, please check the item name again" + "\033[0m")
    else:
        while True:
            while True:
                try:
                    what_to_update = int(
                        input("\nWhat would you like to update? Input:\n1 to update item name\n2 to update item "
                              "qty\n3 to update item price\n"))
                except ValueError:
                    print("Please only enter 1 / 2 / 3")
                else:
                    break

            if what_to_update not in [1, 2, 3]:
                print("Invalid input")
            else:
                if what_to_update == 1:
                    new_name = input("What is the new name of the item? ")
                    new_transaction.update_item_name(item_to_mod, new_name)
                    break
                elif what_to_update == 2:
                    new_qty = int(input("What is the new qty of the item? "))
                    new_transaction.update_item_qty(item_to_mod, new_qty)
                    break
                else:
                    new_price = int(input("What is the new price of the item? "))
                    new_transaction.update_item_price(item_to_mod, new_price)
                    break
