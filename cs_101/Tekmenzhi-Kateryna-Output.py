# Kateryna Tekmenzhi, February 27, 2023 
fhand = open('cs_101/mbox.txt')
outputfile = open('cs_101/emails_output.txt', 'w')
counter_com = 0
counter_edu = 0
counter_org = 0

for line in fhand:
    write_to_file = False
    if line.find('.com') != -1: 
        counter_com += 1
        write_to_file = True

    if line.find('.edu') != -1: 
        counter_edu += 1
        write_to_file = True

    if line.find('.org') != -1: 
        counter_org += 1
        write_to_file = True

    if write_to_file:
        outputfile.write(line)
    
        
print("There were", counter_com, "'.com' email addresses in the file")
print("There were", counter_edu, "'.edu' email addresses in the file")
print("There were", counter_org, "'.org' email addresses in the file")

outputfile.close()
fhand.close()





