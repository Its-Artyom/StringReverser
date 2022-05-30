###
# This is a StringReverser nd as it says on the tin the algorithm reverses a string and outputs it back to the user.
# Made by @its-artyom.
###

# Inputs
original_string = input("Enter a string that you want to reverse: ")
# Reversing the string using slicing
reversed_string = original_string[::-1]
# Outputs
print("Original string: " + original_string)
print("Reversed string: " + reversed_string)