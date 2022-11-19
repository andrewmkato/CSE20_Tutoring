# Lambdas are anonymous functions defined with a special lambda notation
#   derived from lambda calculus in mathematics. The general notation for a
#   lambda function is below. Complete the following three problems.

# lambda input: output

# TODO: Change the following function so that it becomes a lambda.
def add(x, y):
    return x + y # Without using lambda notation.

# TODO: Change the sorted() function such that the key argument is specified as
#       sorting by the second character in each element.
foo = [
    "spam",
    "eggs",
    "ham"
]

foo = sorted(foo)
print(foo)

# TODO: Use a lambda for the map() function to specify that each element in the
#       following list should be squared.
bar = [
    2,
    19,
    3,
    12,
    44,
    32,
    12.5
]