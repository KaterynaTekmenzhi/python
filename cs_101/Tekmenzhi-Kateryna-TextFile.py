# Kateryna Tekmenzhi, February 25, 2023

fhand = open('mbox-short.txt')
count = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:') :
        count += 1
        position = line.find(':')
        piece = line[position+1:]
        value = float(piece)
        print(value)
        
print('Line Count:', count)
            
print('Found '+ str(count) + ' floating point values')



