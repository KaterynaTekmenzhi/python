# Kateryna Tekmenzhi, February 18, 2023

text = "X-DSPAM-Confidence: 0.7285"

# find method
position = text.find(':')

# seperate string after colon
piece = text[position+1:]

# convert seperate string to floating point number
value = float(piece)

# The floating point value is:  
print(value)
