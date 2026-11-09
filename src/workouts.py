workouts = [
    {"workout": "Bench Press", "sets": 3, "reps": 10, "category": "Strength"},
    {"workout": "Squats", "sets": 4, "reps": 12, "category": "Strength"},
    {"workout": "Jogging", "distance": 1.5, "duration": 20, "category": "Cardio"},
    {"workout": "Cycling", "distance": 5, "duration": 30, "category": "Cardio"},
]

completed_workouts = []


def format_workout(exercise):
    """Return a display string for one workout, based on its category."""
    if exercise["category"] == "Strength":
        return f'{exercise["workout"]}: {exercise["sets"]} sets of {exercise["reps"]} reps'
    return f'{exercise["workout"]}: {exercise["distance"]} miles in {exercise["duration"]} minutes'


def add_workout(workout, category, sets=None, reps=None, distance=None, duration=None):
    if not workout:
        print('Workout name cannot be empty.')
        return

    if category == "Strength":
        if sets is None or reps is None or sets <= 0 or reps <= 0:
            print('Sets and reps must be positive numbers.')
            return
        workouts.append({"workout": workout, "sets": sets, "reps": reps, "category": category})
        print(f'Workout "{workout}" added with {sets} sets of {reps} reps!')

    elif category == "Cardio":
        if distance is None or duration is None or distance <= 0 or duration <= 0:
            print('Distance and duration must be positive numbers.')
            return
        workouts.append({"workout": workout, "distance": distance, "duration": duration, "category": category})
        print(f'Workout "{workout}" added with {distance} miles in {duration} minutes!')


def remove_workout(workout_index):
    if workout_index < 0 or workout_index >= len(workouts):
        print('Invalid workout number.')
        return
    exercise = workouts.pop(workout_index)
    print(f'Workout "{exercise["workout"]}" removed.')


def complete_workout(workout_index):
    if workout_index < 0 or workout_index >= len(workouts):
        print('Invalid workout number.')
        return
    exercise = workouts.pop(workout_index)
    completed_workouts.append(exercise)
    print(f'{format_workout(exercise)} marked as done!')


def view_workouts():
    if len(workouts) == 0:
        print('\nNo workouts yet. Add one!')
        return
    print('\nYour Workouts:')
    for index, exercise in enumerate(workouts, start=1):
        print(f'{index}. {format_workout(exercise)}')


def view_completed_workouts():
    if len(completed_workouts) == 0:
        print('\nYou did not complete any workouts yet.')
        return
    print()
    for index, exercise in enumerate(completed_workouts, start=1):
        print(f'{index}. {format_workout(exercise)}')


def clear_workouts():
    workouts.clear()
    completed_workouts.clear()
    print('All workouts cleared!')


def workout_type():
    choice = input("Enter '1' for Strength or '2' for Cardio: ").strip()
    while choice not in ['1', '2']:
        print("Invalid input. Please enter '1' for Strength or '2' for Cardio.")
        choice = input("Enter '1' for Strength or '2' for Cardio: ").strip()
    return "Strength" if choice == '1' else "Cardio"