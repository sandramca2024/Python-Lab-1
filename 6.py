def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def reverse_number(number):
    return int(str(number)[::-1])

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Find the sum of digits")
        print("2. Find the reverse of the number")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice in ('1', '2'):
            while True:
                try:
                    number = int(input("Enter a four-digit number: "))
                    if 1000 <= number <= 9999:
                        break
                    else:
                        print("Please enter a valid four-digit number.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")
            
            if choice == '1':
                digit_sum = sum_of_digits(number)
                print(f"Sum of digits: {digit_sum}")
            elif choice == '2':
                reversed_number = reverse_number(number)
                print(f"Reverse of the number: {reversed_number}")
        elif choice == '3':
            print("THANK YOU!!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Run the main menu
main_menu()
