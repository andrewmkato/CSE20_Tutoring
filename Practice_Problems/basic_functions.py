# Functions are like tasks or actions in a computer program, like driving is to
#   a car. 
# 
# The Python language has many pre-defined functions, like len(), range(), and 
#   print(). It also has functions that serve as methods to objects, indicated
#   via dot notation. A dictionary, for instance, has a method .keys() to access
#   its keys.


# TODO: Define a function that returns True if its input value is divisible by
#       three and returns False if otherwise.
def div_by_three(num) -> bool:
    pass


# TODO: Restructure the function below take up only two lines, including the
#       def keyword declaration.
def exponentiate(base: int, desired_exponent: int, number_of_times=1) -> int:
    total = base
    while number_of_times > 0:
        total = total ** desired_exponent
        number_of_times -= 1 
    return total

print(exponentiate(2, 4)) # Should return 16.
print(exponentiate(2, 4, 3)) # Should return 1.8446744 * 10^19.