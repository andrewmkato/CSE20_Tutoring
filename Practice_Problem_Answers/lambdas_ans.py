# Lambdas are anonymous functions defined with a special lambda notation
#   derived from lambda calculus in mathematics. The general notation for a
#   lambda function is below. Complete the following three problems.

# lambda input: output

# TODO: Turn the following normal function into a one-line lambda function.
add = lambda x,y: x+y # Using lambda notation.

# TODO: Change the sorted() function such that the key argument is specified as
#       sorting by the second character in each element.
foo = [
    "spam",
    "eggs",
    "ham"
]

foo = sorted(foo, key=lambda word: word[1])
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

output = map(lambda num: num*num, bar)
print(list(output))