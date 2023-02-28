# Kateryna Tekmenzhi, February 26, 2023

while True:
    score = input("Enter score: ")
    try:
        score = float(score)
    except:
        print("Bad score")
        continue 
    break
    
# precondition that the parameter score should be a float. 
def computegrade(score):
    # conditional for grading scale
    if score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    elif score < 0.6:
        grade = 'F'
    return grade

output = computegrade(score)
print("Grade:", output)

## confirms that the output is a string
#print(type(output))
