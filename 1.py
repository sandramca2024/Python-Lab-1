# Function to get a list of numbers from user input
def get_numbers_from_user():
    input_string = input("Enter numbers separated by spaces: ")
    number_list = list(map(int, input_string.split()))
    return number_list

# Get numbers from user
numbers = get_numbers_from_user()

# (a) Sum all the items of the list
sum_of_items = sum(numbers)
print(f"Sum of all items: {sum_of_items}")

# (b) Multiply all the items using a loop
product_of_items = 1
for number in numbers:
    product_of_items *= number
print(f"Product of all items: {product_of_items}")

# (c) Get the largest number from the list
largest_number = max(numbers)
print(f"Largest number: {largest_number}")

# (d) Get the smallest number from the list
smallest_number = min(numbers)
print(f"Smallest number: {smallest_number}")
