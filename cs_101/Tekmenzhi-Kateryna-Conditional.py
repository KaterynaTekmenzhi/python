# Kateryna Tekmenzhi, February 18, 2023

# prompt user to enter score between 0.0 and 1.0
score=input("Enter score: ")

# conditional for non integar values
try:
    score = float(score)
except:
    print("Bad score")
    exit(0)

# conditional for grading scale
if float(score) >= 0.9 and float(score) <= 1.0:
    print("A")
elif float(score) >= 0.8 and float(score) <= 0.9:
    print("B")
elif float(score) >= 0.7 and float(score) <= 0.8:
    print("C")
elif float(score) >= 0.6 and float(score) <= 0.7:
    print("D")
elif float(score) >= 0.0 and float(score) <= 0.6:
    print("F") 

# error message for any integar outside of 0.0 - 1.0
else:
    print("Please type a score between 0.0 and 1.0")
