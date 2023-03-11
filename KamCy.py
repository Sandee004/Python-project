import time, os
todo= []

def addItems():
    name= input("\nItem\n>>")
    price= input("Price\n>>")
    set= [name, price]
    todo.append(set)
    time.sleep(0.5)
    print("Added")
    time.sleep(0.9)
    os.system("clear")


def removeItems():
    time.sleep(1)
    os.system("clear")
    cancel = input("What item do you want to remove? ")
    for row in todo:
        if cancel in row:
            todo.remove(row)
            time.sleep(0.5)
            print("Removed")
    if cancel not in row:
        print("That item doesn't exist")
    time.sleep(1)
    os.system("clear")
        

def viewItems():
    time.sleep(1)
    os.system("clear")
    #loop through the todo lost amd show each on a new line
    for row in todo:
        for item in row:
            print(item, end= " || ")
        print()
    print()
    time.sleep(1.6)
    os.system("clear")


def computeTotal():
    #Give the computer one second before clearing the screen
    time.sleep(1)
    os.system("clear")
    #generate a new list with the prices
    #loop through each row and get the item with index 1 which is the price. Then convert it from a string to a float
    priceList= [float(item[1]) for item in todo]
    total = 0
    #loop through the new list and add all elements to total
    for ele in range(0, len(priceList)):
        total = total + priceList[ele]
    print("Total price of items in cart is ", total)
    time.sleep(1.2)
    os.system("clear")


#So it keeps appearing
while True:
    operation = input("Welcome to the main menu\n1. Add a new item\n2. Display items in your cart\n3. Remove an item\n4. Compute the total\n5. Quit\n>>>")
    if operation == "1":
        addItems()
    if operation == "2":
        viewItems()
    if operation == "3":
        removeItems()
    if operation == "4":
        computeTotal()
    if operation == "5":
        break
