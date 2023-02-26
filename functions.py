# a function is a named sequence of statements that performs a computation. When you define a function, you specify the name and the sequence of statements. Later, you can “call” the function by name
type(32)
print(type(32)) #returns <class 'int'>

#Built in functions
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
