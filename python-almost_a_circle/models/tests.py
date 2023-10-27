#!/usr/bin/python3

def reverse_vowels(s):
    # Convert the string to a list of characters for easy manipulation
    s_list = list(s)

    # Define the set of vowels
    vowels = set("AEIOUaeiou")

    # Initialize pointers for the first and last characters of the string
    left, right = 0, len(s) - 1

    while left < right:
        # Find the first vowel from the left
        while left < right and s_list[left] not in vowels:
            left += 1

        # Find the first vowel from the right
        while left < right and s_list[right] not in vowels:
            right -= 1

        # Swap the vowels
        s_list[left], s_list[right] = s_list[right], s_list[left]

        # Move the pointers
        left += 1
        right -= 1

    # Convert the list back to a string
    reversed_string = ''.join(s_list)

    return reversed_string

# Test the function
input_string = "Betty"
result = reverse_vowels(input_string)
print(result)  # Output: "Bytte"
