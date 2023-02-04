from tabulate import tabulate

num_of_transaction = 1


class Transaction:
    def __init__(self):
        self.transaction_id = num_of_transaction
        self.item_name = []
        self.qty = []
        self.price = []
        self.num_of_items = 0

    def add_item(self, added_item_name, added_qty, added_price):
        self.item_name.append(added_item_name)
        self.qty.append(added_qty)
        self.price.append(added_price)
        self.num_of_items += 1

    def check_order(self):
        self.item_index = list(range(1, len(self.item_name) + 1))
        self.totprice_per_item = []
        for i in range(0, len(self.item_name)):
            self.totprice_per_item.append(self.qty[i] * self.price[i])
        print(tabulate(
            {"No.": self.item_index, "Item Name": self.item_name, "Quantity": self.qty, "Price/Item": self.price,
             "Total Price": self.totprice_per_item}, headers="keys", tablefmt="github"))

    def update_item_name(self, prev_name, new_name):
        for i in range(0, self.num_of_items):
            if self.item_name[i] == prev_name:
                self.item_name[i] = new_name
                print(f"{prev_name} has been successfully changed to {new_name}")

    def update_item_qty(self, in_item_name, new_qty):
        for i in range(0, self.num_of_items):
            if self.item_name[i] == in_item_name:
                self.qty[i] = new_qty
                print(f"The qty of {in_item_name} has been successfully changed to {new_qty}")

    def update_item_price(self, in_item_name, new_price):
        for i in range(0, self.num_of_items):
            if self.item_name[i] == in_item_name:
                self.price[i] = new_price
                print(f"The price of {in_item_name} has been successfully changed to {new_price}")

    def delete_item(self, del_item_name):
        if del_item_name not in self.item_name:
            print("\033[1m" + "\033[91m" + "Item not found, please check the item name again" + "\033[0m")
        else:
            for i in range(0, self.num_of_items):
                if self.item_name[i] == del_item_name:
                    self.item_name.pop(i)
                    self.qty.pop(i)
                    self.price.pop(i)
                    self.qty_price.pop(i)
                    self.num_of_items -= 1
                    break
            print(f"{del_item_name} has been deleted")

    def reset_transaction(self):
        self.item_name = []
        self.qty = []
        self.price = []
        self.qty_price = []
        self.num_of_items = 0
        print("All item in this transaction has been deleted")

    def total_price(self):
        self.calc_total_price = 0
        for i in range(0, self.num_of_items):
            self.calc_total_price += (self.qty[i] * self.price[i])
        if self.calc_total_price > 500000:
            self.calc_total_price = 0.9 * self.calc_total_price
            print("You get 10% discount for purchasing above Rp 500.000,-")
        elif self.calc_total_price > 300000:
            self.calc_total_price = 0.92 * self.calc_total_price
            print("You get 8% discount for purchasing above Rp 300.000,-")
        elif self.calc_total_price > 200000:
            self.calc_total_price = 0.95 * self.calc_total_price
            print("You get 5% discount for purchasing above Rp 200.000,-")
        print(f"Your total price is: Rp. {int(self.calc_total_price)}")
