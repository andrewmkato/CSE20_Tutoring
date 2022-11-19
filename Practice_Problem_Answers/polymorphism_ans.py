# Polymorphism is when something transforms its behavior depending on a given
#   situation. A real-world example is that a single person could simultaneously
#   be a mother, a wife, a grandmother, and a daughter.

# TASK: Demonstrate at least two examples in Python in which polymorphism
#   natively occurs. This could involve creating your own class, creating an
#   expressions with certain operators, or something else.

# Here's an example for assistance.
text1 = "Hello"
text2 = "world!"
phrase = text1 + text2 # Concatenation.
print(phrase)

num1 = 12
num2 = 3
sum = num1 + num2 # Addition.
print(sum)

# EXAMPLE ONE HERE
foo = "Oh what a to-do to die today at a minute or two 'till two."
print(len(foo)) # len() returns the number of characters in the string.

bar = [1, 2, 3, 55, 13.02]
print(len(bar)) # Now, returns the number of elements in the data structure.



# EXAMPLE TWO HERE
baz = 40
print("%.5f" % baz) # The f-symbol serves to specify baz as a float.
print(f"{baz:.5f}") # The first f-symbol now specifies a formatted string.