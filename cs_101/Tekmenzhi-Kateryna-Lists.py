# Kateryna Tekmenzhi, February 25, 2023

fhand = open('mbox-short.txt')
count = 0

for line in fhand:
    if line.startswith('From ') :
        count += 1
        mylist = line.split(' ')
        
        print(mylist[1])
        
    
print('Line Count:', count)

