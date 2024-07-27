def print_color_list(color_list):
    for color in color_list:
        print(color)

def add_colors(color_names, color_codes):
    while True:
        name = input("Enter the color name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        code = input("Enter the color code: ")
        color_names.append(name)
        color_codes.append(code)

def main_menu():
    # Given lists
    color_names = ["Black", "Red", "Maroon", "Yellow"]
    color_codes = ["000000", "FF0000", "800000", "FFFF00"]

    while True:
        print("\nMenu:")
        print("1. Print Current Colors")
        print("2. Add More Colors")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            # Convert lists to a list of dictionaries and print
            color_list = [{'colorName': name, 'colorCode': code} for name, code in zip(color_names, color_codes)]
            print("\nCurrent Colors:")
            print_color_list(color_list)
        elif choice == '2':
            add_colors(color_names, color_codes)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Run the main menu
main_menu()



