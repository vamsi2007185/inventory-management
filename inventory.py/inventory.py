inventory = {}

def add_item():
    name = input("Enter item name: ")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    inventory[name] = [qty, price]
    print("Item added successfully!")

def update_item():
    name = input("Enter item name to update: ")
    if name in inventory:
        qty = int(input("Enter new quantity: "))
        price = float(input("Enter new price: "))
        inventory[name] = [qty, price]
        print("Item updated!")
    else:
        print("Item not found!")

def display_items():
    if not inventory:
        print("Inventory is empty!")
    else:
        print("\n--- Inventory ---")
        for item, details in inventory.items():
            print(f"{item} -> Quantity: {details[0]}, Price: {details[1]}")

while True:
    print("\n1. Add Item")
    print("2. Update Item")
    print("3. Display Items")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_item()
    elif choice == '2':
        update_item()
    elif choice == '3':
        display_items()
    elif choice == '4':
        break
    else:
        print("Invalid choice!")