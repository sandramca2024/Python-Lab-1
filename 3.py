def print_pattern_1(rows):
    for i in range(rows):
        # Print leading spaces
        print(' ' * (rows - i - 1), end='')
        # Print characters
        for j in range(i + 1):
            print(chr(65 + j), end=' ')
        print()

def print_pattern_2(rows):
    for i in range(rows):
        # Print stars
        print('* ' * (i + 1))

def menu():
    while True:
        print("\nMenu:")
        print("1. Print Pattern 1")
        print("2. Print Pattern 2")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            rows = int(input("Enter the number of rows for Pattern 1: "))
            print("\nPattern 1:")
            print_pattern_1(rows)
        elif choice == '2':
            rows = int(input("Enter the number of rows for Pattern 2: "))
            print("\nPattern 2:")
            print_pattern_2(rows)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Run the menu
menu()
