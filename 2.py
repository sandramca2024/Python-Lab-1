# Given list of strings
given_list = ['abc', 'xyz', 'aba', '1221']

# Iterate over the list with index
for index, string in enumerate(given_list):
    # Check if the string is non-empty and if the first and last characters are the same
    if len(string) > 0 and string[0] == string[-1]:
        print(f"String: '{string}', Index: {index}")
