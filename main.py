from Transaction import Transaction, num_of_transaction
from user_input import *

while True:
    new_transaction = input("Do you want to start a new transaction? (Y/N) ")

    if new_transaction.upper() == "Y":
        new_transaction = Transaction()
        print(f"Your order ID is #{num_of_transaction}")
        request_add_item(new_transaction)
        while True:
            while True:
                try:
                    next_action = int(input(
                        "\nWhat would you like to do next? Input:\n1 to add more item\n2 to update existing item\n3 "
                        "to remove item\n4 to reset transaction\n5 to check order summary\n"))
                except ValueError:
                    print("Please only enter 1 / 2 / 3/ 4/ 5")
                else:
                    break

            if next_action not in [1, 2, 3, 4, 5]:
                print("Invalid input")
            else:
                if next_action == 1:
                    request_add_item(new_transaction)
                elif next_action == 2:
                    item_to_modify = input("What is the name of item to update: ")
                    request_update_item(new_transaction, item_to_modify)
                elif next_action == 3:
                    item_to_del = input("Input the name of item to delete: ")
                    new_transaction.delete_item(item_to_del)
                elif next_action == 4:
                    new_transaction.reset_transaction()
                else:
                    new_transaction.check_order()
                    new_transaction.total_price()
                    pay_or_edit = int(input("\nWhat would you like to do next? Input:\n1 to confirm order and pay\n2 "
                                            "to continue to add or edit items\n"))
                    if pay_or_edit not in [1, 2]:
                        print("Invalid input")
                    else:
                        if pay_or_edit == 1:
                            if len(new_transaction.item_name) < 1:
                                print("There is no item in your transaction, please enter an item")
                            else:
                                print("Your order is confirmed, please proceed to payment")
                                num_of_transaction += 1
                            break
                        else:
                            pass
