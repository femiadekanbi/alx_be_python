def display_menu():
    print("Shoppibg List Manager")
    print("Add Item")
    print("Remove Item")
    print("View List")
    print("Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to the list.")
    
        elif choice == "2":
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f'{item} has been removed from the list.')

            else:
                print(f"{item} is not in the shopping list.")
  
        elif choice == "3":
            if shopping_list:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}, {item}")
            else:
                print("Your shopping list is empty.")
     
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()