import os
from workouts import (add_workout, remove_workout, complete_workout,view_workouts, view_completed_workouts, workout_type,)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def handle_choice(choice):
    """Return False to exit the program, True to keep going."""
    if choice == "1":
        category = workout_type()
        print(f"You selected {category} workout.")
        workout = input("What workout would you like to add? ").strip()

        if category == "Strength":
            sets = int(input("Enter number of sets: "))
            reps = int(input("Enter number of reps: "))
            add_workout(workout, category, sets=sets, reps=reps)
        elif category == "Cardio":
            distance = float(input("Enter distance (in miles): "))
            duration = float(input("Enter duration (in minutes): "))
            add_workout(workout, category, distance=distance, duration=duration)

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


def show_menu():
    is_running = True
    while is_running:
        print("\nMenu:")
        print("1. Add Workout")
        print("2. Remove Workout")
        print("3. Complete Workout")
        print("4. View Workouts")
        print("5. Exit")

        choice = input("What would you like to do? Choose an option (1-5): ").strip()

        try:
            is_running = handle_choice(choice)
        except ValueError:
            print("Please enter a valid number.")

        if is_running:
            input("\nPress Enter to continue...")
            clear_screen()