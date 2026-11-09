import os
from workouts import add_workout, remove_workout, complete_workout, view_workouts, view_completed_workouts


def show_menu():
    is_running = True
    while is_running:
        print("\nMenu:")
        print("1. Add Workout")
        print("2. Remove Workout")
        print("3. Complete Workout")
        print("4. View Workouts")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        try:
            is_running = handle_choice(choice)
        except ValueError:
            print("Please enter a whole number.")

        if is_running:
            input("\nPress Enter to continue...")
            clear_screen()
            
def handle_choice(choice):
    """Return False to exit the program, True to keep going."""
    if choice == "1":
        workout = input("What workout would you like to add? ").strip()
        sets = int(input("Enter number of sets: "))
        reps = int(input("Enter number of reps: "))
        add_workout(workout, sets, reps)
    elif choice == "2":
        view_workouts()
        index = int(input("Enter the number of the workout to remove: ")) - 1
        remove_workout(index)
    elif choice == "3":
        print("Which workout did you complete?")
        view_workouts()
        index = int(input("Enter the number of the workout you completed: ")) - 1
        complete_workout(index)
    elif choice == "4":
        print("Here are the current workouts:")
        view_workouts()
        print("\nHere are the completed workouts:")
        view_completed_workouts()
    elif choice == "5":
        return False
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
    return True

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
