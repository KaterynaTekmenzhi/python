# Kateryna Tekmenzhi, February 25, 2023

total = 0.0
count = 0
while True :
    text = input('Enter a number: ')
    if text == 'done' :
        break
    try:
        ftext = float(text)
    except:
        print('Invalid input')
        continue
    count = count + 1
    total = total + ftext

print('Total: ',int(total))
print('Count: ',count)
print('Average: ',total/count)

    
    
