# Recursion is an intuitive and useful method of constructing functions in
#   Python. In essence, use-cases involve a given function calling itself in
#   its definition, until a certain state is reached.

# TASK: Create a function that divides a number by two until it is less than
#   or equal to ten, at which it returns the end result.

# For assistance, here is a non-recursive version.
def nonrecursive_divide(x):
    while i > 10:
        i /= 2 # i = i / 2
    
    return i

# TO-DO
def recursive_divide(x):
    return recursive_divide(x/2) if x > 10 else x

if __name__ == "__main__":
    print(recursive_divide(16)) # Should return 8.
    print(recursive_divide(168923)) # Arbitrarily large number.