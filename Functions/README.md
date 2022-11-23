# The Concept and Implementation of Functions

How do you normally think of the word _function_, outside of computer programming? At least one idea that most people think of is along the lines of a definition from [_Merriam-Webster_](https://www.merriam-webster.com/thesaurus/function):
- _The action for which a person or thing is specially fitted or used for which a thing exists._

An example you've likely heard me bring up involves cars. What would you say is the function of a car? Here are some common examples I hear:
- _To transport something or someone._
- _To travel over some distance._
- _To be driven or drive to a location._
- _To store luggage, people, or some other items._
- _To provide shelter._

Each of these descriptions are valid, and they represent various practical functions, or tasks, of a car. Let's imagine that a computer programmer is creating a virtual car in, say, some online game. On a surface level, that car needs to at least be capable of traveling some virtually-represented distance. It's task is to be driven, in this case, by some online user. We can say this car has a function, which the programmer needs to define. Let's name this function _drive_. In Python, a simplified representation of this is below.

```
drive(pressure_on_gas_pedal: int, psi: int) -> bool:
    if pressure_on_gas_pedal >= psi:
        return True # If the pressure is greater than or equal to the pre-set PSI, the car will move.
    else:
        return False # If the pressure is less than the needed PSI, the car won't move.
```
In this scenario, a minimum amount of PSI, pounds per square inch, must be applied to the virtual gas pedal for the user to move the car. For this function, drive(), the PSI needed to move the car, and the user's actual PSI, are taken as input. This is inside the parentheses. The output, noted by the arrow syntax, is a boolean value, AKA true or false. If true, the car will start moving; if false, it will remain stationary. An implementation example of this function is below. Imagine that this function is a method of a pre-defined car class, indicated by dot notation. In other words, all cars we create are able to be driven.

```
user_car = Car()

user_car.drive(pressure_on_gas_pedal=55, psi=40) # True, since the actual pressure is greater than the minimum needed.
```
The .drive() function receives, as input, a required minimum of 40 PSI in order to move the user's car. Additionally, the user applies 55 PSI to the car's figurative gas pedal. Since 55 is greater than 40, the car will move in the game. Usually, though, a car will need to move for a continuous period of time. Oftentimes, especially in a race, the car should stay in motion for a long distance.

```
drive(pressure_on_gas_pedal: int, psi: int) -> bool:
    while pressure_on_gas_pedal >= psi:
        yield True # If the pressure is greater than or equal to the pre-set PSI, the car will move.
    else:
        yield False # If the pressure is less than the needed PSI, the car won't move.
```
