# Kateryna Tekmenzhi, March 1, 2023

# Write a program that uses random to generate a random grade (4.00 grading scale) inside a loop, and that loop keeps running until it generates a 4.00 GPA. Once you have randomly generated a 4.00, print the number of iterations it took to randomly generate.

# import random library
import random

# initialize variables
count = 0
grade = 0

# loop that runs until grade is 4.00
while grade != 4.00:
    grade = round(random.uniform(0.00, 4.00),2)
    count += 1
    print(grade)

# print the number of iterations
print("It took", count, "iterations to generate a 4.00 GPA")


    



