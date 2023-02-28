#Built in functions

# a function is a named sequence of statements that performs a computation. When you define a function, you specify the name and the sequence of statements. Later, you can “call” the function by name
type(32)
print(type(32)) #returns <class 'int'>

# abs returns the absolute value of a number
abs(-32)

# max returns the largest character in a string
max('this is so Fun!z*(%$#@!')

# min returns the smallest character in a string
min('Hello world')

# len returns the full length of the string numerically 
len('Hello world')

print(abs(-32))
print(len('Hello world')) #returns 11
print(max('this is so Fun!z*(%$#@!')) #returns z
print(min('Hello world')) #returns space


# Type conversion functions

# int converts a string to an integer
int('32')
print(int('32')) #returns 32

# float converts a string to a floating point number
float('32')
print(float('32')) #returns 32.0

# str converts a value to a string
str(float(32))
print(str(float(32))) #returns 32.0

# math functions

# math functions are similar to built in functions, but they require you to import the math module first
import math
print(math) #returns <module 'math' (built-in)>

# The module object contains the functions and variables defined in the module. To access one of the functions, you have to specify the name of the module and the name of the function, separated by a dot (also known as a period). This format is called dot notation.
print(math.pi) #returns 3.141592653589793

signal_power = 9
noise_power = 10
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
radians = 0.7
height = math.sin(radians)


degrees = 45
radians = degrees / 360.0 * 2 * math.pi
p_radians = math.sin(radians)
sqrt_p = math.sqrt(2) / 2.0

print(decibels) #returns 3.010299956639812
print(height) #returns 0.644217687237691
print(p_radians) #returns 0.7071067811865476
print(sqrt_p) #returns 0.7071067811865476

# random numbers
# the random module provides functions that generate random numbers in a variety of ways. The function random returns a random float between 0.0 and 1.0 (including 0.0 but not 1.0)
import random
for i in range(10):
    x = random.random()
    print(x)

rr = random.randint(5, 10) 
print(rr) #returns a random integer between 5 and 10

t = [1, 2, 3]
rc = random.choice(t)
print(rc) #returns a random element from a sequence

# Adding New Functions
# A function definition specifies the name of a new function and the sequence of statements that run when the function is called. Once we define a function, we can reuse the function over and over throughout our program.
# def keyword tells python that you are defining a function. Memory placeholder
def print_lyrics():
    print("So far python is looking great, feeling great, and I'm ready to code!")
    print('Its snowing outside.. march is just around the corner.. here on the west coast')

# defining a function creates a variable with the same name
print(print_lyrics) #returns <function print_lyrics at 0x7f9c1c0b0c20>

# the type of this variable is function
print(type(print_lyrics)) #returns <class 'function'>

# to run the function, you have to call it
print_lyrics() #returns So far python is looking great, feeling great, and I'm ready to code! Its snowing outside.. march is just around the corner.. here on the west coast

# you can use functions inside other functions
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
repeat_lyrics()

# parameters and arguments
# some of the functions we have seen require arguments. For example, when you call math.sin you pass a number as an argument. Some functions take more than one argument: math.pow takes two, the base and the exponent.
# inside the function, the arguments are assigned to variables called parameters. Here is an example of a user-defined function that takes an argument:
def print_twice(bruce):
    print(bruce)
    print(bruce)
print_twice('spam') #returns spam spam
print_twice(1738) #returns 1738 1738

# the name of the variable we pass as an argument (bruce) has nothing to do with the name of the parameter (bruce). It doesn’t matter what the name of the variable is; what matters is that the variable we pass as an argument is the right type of thing.
# this function does something kind of similar to the previous one, but it takes two arguments and prints each one twice:
def print_twice(bruce, bruce2):
    print(bruce)
    print(bruce2)
print_twice('spam', 'eggs') #returns spam eggs

# the order of the arguments has to match the order of the parameters
# this function takes two arguments, a first name and a last name, and prints them in reverse order:
def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat, cat)
line1 = 'Bing tiddle '
line2 = 'tiddle bang.'
cat_twice(line1, line2) #returns Bing tiddle tiddle bang. Bing tiddle tiddle bang.

import math
print_twice(math.pi, math.pi) #returns 3.141592653589793 3.141592653589793


