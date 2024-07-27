def print_even_squares(start, end):
    print(f"Even numbers and their squares from {start} to {end - 1}:")
    for number in range(start, end):
        if number % 2 == 0:
            print(f"Number: {number}, Square: {number ** 2}")

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Print even numbers and their squares")
        print("2. Exit")

        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            print_even_squares(start, end)
        elif choice == '2':
            print("THANK YOU!!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

# Run the main menu
main_menu()
