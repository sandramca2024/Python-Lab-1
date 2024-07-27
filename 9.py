def extract_last_character(word):
    # Extract the last character of the provided word
    return word[-1] if word else ''

def main():
    while True:
        # Prompt the user to enter a word
        word = input("Enter a word (or type 'exit' to quit): ")
        
        if word.lower() == 'exit':
            print("Exiting...")
            break

        # Extract the last character
        last_character = extract_last_character(word)

        # Print the last character
        print(f"The last character of the word is: {last_character}")

# Run the main function
main()
