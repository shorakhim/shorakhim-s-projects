workouts = [
    {"workout": "Bench Press", "sets": 3, "reps": 10},
    {"workout": "Squats", "sets": 4, "reps": 12},
]

completed_workouts = []

def add_workout(workout, sets, reps):
    if not workout:
        print('Workout name cannot be empty.')
        return
    if sets <= 0 or reps <= 0:
        print('Sets and reps must be positive integers.')
        return
    workouts.append({"workout": workout, "sets": sets, "reps": reps})
    print(f'Workout "{workout}" added with {sets} sets of {reps} reps!')

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
    print(f'Workout "{exercise["workout"]}" ({exercise["sets"]} sets of {exercise["reps"]} reps) marked as done!')

def view_workouts():
    if len(workouts) == 0:
        print('\nNo workouts yet. Add one!')
        return
    print('\nYour Workouts:')
    for index, exercise in enumerate(workouts, start=1):
        print(f'{index}. {exercise["workout"]}: {exercise["sets"]} sets of {exercise["reps"]} reps')

def view_completed_workouts():
    if len(completed_workouts) == 0:
        print('\nYou did not complete any workouts yet.')
        return
    print()
    for index, exercise in enumerate(completed_workouts, start=1):
        print(f'{index}. {exercise["workout"]}: {exercise["sets"]} sets of {exercise["reps"]} reps')

def clear_workouts():
    workouts.clear()
    print('All workouts cleared!')