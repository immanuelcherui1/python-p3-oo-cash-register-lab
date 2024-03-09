#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.items.append((title, price, quantity))
        self.total += price * quantity

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            self.total -= last_item[1] * last_item[2]
        else:
            print("There are no items to void.")

    def apply_discount(self):
        if self.discount > 0:
            self.total -= self.total * self.discount / 100
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")
        return self.total
