def is_leap_year(year):
    # Returns True if the year is a leap year, otherwise False
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(month, year=None):
    # Define the number of days for each month
    months_days = {
        "January": 31,
        "February": 28,  # Default to 28, will handle leap years separately
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    
    # Get the number of days for the given month
    days = months_days.get(month, None)
    
    if month == "February" and year is not None:
        if is_leap_year(year):
            days = 29

    return days

def main():
    while True:
        # Display the menu
        print("\nMenu:")
        print("1. Enter a month name")
        print("2. Enter a month name with a specific year")
        print("3. Exit")
        
        # Get user's choice
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            # Enter month name
            month = input("Enter the month name: ").capitalize()
            days = get_days_in_month(month)
            if days is not None:
                print(f"The number of days in {month} is: {days}")
            else:
                print("Invalid month name. Please enter a valid month.")
        
        elif choice == '2':
            # Enter month name and year
            month = input("Enter the month name: ").capitalize()
            year = int(input("Enter the year: "))
            days = get_days_in_month(month, year)
            if days is not None:
                print(f"The number of days in {month} is: {days}")
            else:
                print("Invalid month name. Please enter a valid month.")
        
        elif choice == '3':
            # Exit the program
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Run the main function
main()
