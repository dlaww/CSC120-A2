from computer import *

class ResaleShop:

    # What attributes will it need?
    inventory: list
    bank : int
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []
        self.bank = 50000

    # What methods will you need?
    # buying a computer + adding it to inventory
    def buy(self, c: Computer):
        self.inventory.append(c)
        print("added", c)
        print(self.inventory)
    
    # selling a computer + removing it from inventory
    def sell(self, c: Computer):
        if c in self.inventory:
            self.inventory.remove(c)
            print("removed", c)
            print(self.inventory)
        else:
            print("Computer not in inventory")
            
    # refurbish + increasing price
    def refurbished(self, c: Computer):
        if c.year_made < 2000:
            c.price = 50         # old computer, salvage parts?
        elif c.year_made < 2012:
            c.price = 250       # 10+ yr old computer, in workable condition
        elif c.year_made < 2020:
            c.price = 750       # 3+ yr old computer
        else:
            c.price = 1000      # like new computer

def main():
    # buy the computer
    ResaleShop.buy.c: Computer
    print("Computer purchased")

    # print the manifest

    # sell the computer
    #print the inventory manifest
main()
