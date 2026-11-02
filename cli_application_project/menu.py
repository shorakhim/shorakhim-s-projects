def show_menu():
    is_running = True
    while is_running:
        print("\nMenu:")
        print("1. Play a round")
        print("2. View Statistics")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("You chose option 1")
        elif choice == "2":
            print("You chose option 2")
        elif choice == "3":
            is_running = False
        else:
            print("Invalid choice. Please try again.")