def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # تعريف القائمة مباشرة

    while True:
        display_menu()  # استدعاء الدالة بشكل واضح
        choice = input("Enter your choice (1-4): ")

        if choice.isdigit():  # التأكد من أن المدخل رقم
            choice = int(choice)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added.")
            else:
                print("No item entered.")

        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed.")
            else:
                print(f"'{item}' not found in the list.")

        elif choice == 3:
            if shopping_list:
                print("Shopping List:")
                for i, itm in enumerate(shopping_list, 1):
                    print(f"{i}. {itm}")
            else:
                print("The shopping list is empty.")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
