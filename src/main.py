# Start your CLI app here.
#
# Run it with:  python3 src/main.py
#
# The brief is in PROJECT.md.

from menu import show_menu
 
def main():
    print('Welcome to the Workout Tracker!')
    show_menu()
    print('Goodbye!')

if __name__ == "__main__":
    main()