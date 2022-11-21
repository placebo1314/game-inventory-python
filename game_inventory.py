import csv
import os

def add_to_inventory(inventory, added_items):
    for key in added_items:
        inventory[key] = 1 if key not in inventory else inventory[key] + 1
    return inventory

def remove_from_inventory(inventory, removed_items):
    for key in removed_items:
        try:
            if inventory[key] > 1:
                inventory[key] -= 1
            elif inventory[key] <= 1:
                del inventory[key]
        except:
            print("Not found the '{0}' item in the inventory!".format(key))
    return inventory

def print_table(inventory, order = None):
    list1 = []
    if order == "count,asc":
        sorted_items = sorted(inventory.items(), key=lambda x: x[1])
    elif order == "count,desc":
        sorted_items = sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    else:
        sorted_items = list(inventory.items())
    list1.append("-----------------\nitem name | count\n-----------------\n")
    for c in range(0, len(sorted_items)):
        list1.append("{0:>9} |{1:>6}\n".format(sorted_items[c][0], sorted_items[c][1]))
    list1.append("-----------------")
    print(''.join(list1))

def import_inventory(filename="import_inventory.csv"):
    list1 = []
    inventory={}
    try:
        with open(filename, 'r+') as items_file:
            reader = csv.reader(items_file)
            for item in reader:
                list1 += item
            return add_to_inventory(inventory, list1)
    except:
        print("File '{0}' not found!".format(filename))

def export_inventory(inventory, filename='import_inventory.csv'):
    list1 = []
    try:
        with open(filename, 'w') as items_file:
            writer = csv.writer(items_file)
            while len(inventory.keys()) > 0 :
                for item in list(inventory):
                    list1.append(item)
                    inventory = remove_from_inventory(inventory, [item])
            writer.writerow(list1)
    except:
        print(
            "You don't have permission creating file '{0}'!".format(filename))

def clr_scr():
        os.system('cls') if os.name == "nt" else os.system('clear')

def main():
    x = "0"
    while x != "q":
        x = input("1: add item, 2: delete item, 3: listing items ('q': Quit) \n")
        inventory = import_inventory()
        if x == "1":
            print("Take the new items. (separetid with ' '): ")
            added_items = input("").split(" ")
            print_table(add_to_inventory(inventory, added_items))
            export_inventory(inventory)
        elif x == "2":
            print("Take the unused items. (separetid with ' '): ")
            removed_items = input("").split(" ")
            print_table(remove_from_inventory(inventory, removed_items))
            export_inventory(inventory)
        elif x == "3":
            clr_scr()
            print_table(inventory)

main()
