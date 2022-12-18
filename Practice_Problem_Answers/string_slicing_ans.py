# Think of slicing like grabbing a piece of a larger cake, except that piece
# is a copy rather than the real thing. In Python, strings are immutable, but
# you can pull out copies of string slices to manipulate them as needed.

# TODO: Use slice notation to assign to a new variable the first half of
#       the following string.

original_string = "loremipsumdolorsitamet"

new_version = original_string[:int(len(original_string)/2)]
print(new_version)


# TODO: Now, reassign to that variable every third letter of original_string.

new_version = original_string[::3]
print(new_version)

# TODO: Create a new variable, odd_nums, and assign to it a string containing
#       only the numbers in num_string that are odd. Plan how you might do this.
#       How would you be able to test each character in the string as a number?

num_string = "28393745129381"

# odd_nums should equal "39375931"

num_string = list(num_string) # Typecasting the string into a list.

# Using a list comprehension to filter out even numbers.
odd_collection = [num for num in num_string if int(num)%2 != 0]

odd_nums = "" # String that will take on each string-number from the collection.
for i in odd_collection:
    odd_nums += i # Adding each string-number to the list.

print(odd_nums) # "39375931"