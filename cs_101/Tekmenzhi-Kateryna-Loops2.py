# Kateryna Tekmenzhi, March 1, 2023

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


    



