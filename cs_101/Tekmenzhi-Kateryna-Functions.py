# Kateryna Tekmenzhi, February 25, 2023

def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        reg = rate * 40
        comp = (hours - 40.0) * (rate * 1.5)
        pay = reg + comp
    return pay

h = float(input('How many hours?:'))
r = float(input('What is your hourly rate?:'))

print("Pay:", computepay(h,r))


