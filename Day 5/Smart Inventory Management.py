inventory = {}
categories = set()

while True:

    print("\n1.Add Product")
    print("2.Search Product")
    print("3.Display Inventory")
    print("4.Inventory Report")
    print("5.Delete Product")
    print("6.Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        pid = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        category = input("Enter Category: ")
        qty = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))

        inventory[pid] = {
            "name": name,
            "category": category,
            "qty": qty,
            "price": price
        }

        categories.add(category)
        print("Product Added")

    elif choice == "2":

        key = input("Enter Product ID or Name: ").lower()

        result = []

        for pid, data in inventory.items():
            if key == pid.lower() or key in data["name"].lower():
                result.append((pid, data))

        if len(result) == 0:
            print("Product Not Found")
        else:
            for item in result:
                print(item)

    elif choice == "3":

        for pid, data in inventory.items():
            print(pid, data)

    elif choice == "4":

        total_qty = 0
        total_value = 0

        for data in inventory.values():
            total_qty += data["qty"]
            total_value += data["qty"] * data["price"]

        print("Total Items:", total_qty)
        print("Total Value:", total_value)
        print("Categories:", categories)

    elif choice == "5":

        pid = input("Enter Product ID: ")

        if pid in inventory:
            del inventory[pid]
            print("Product Deleted")
        else:
            print("Product Not Found")

    elif choice == "6":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")