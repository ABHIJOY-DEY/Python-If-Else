import math
unit = int(input())
price = 0.00
surprice = 0.00
if unit>50:
    if unit>150:
        if unit>250:
            unit = unit - 250
            price = 220 + unit*1.5
        else:
            unit = unit - 150
            price = 100 + unit*1.2
    else:
        unit = unit - 50
        price = 25 + unit*0.75
else:
    price = unit*0.5

surprice = price + 0.2*price
surpriceStr = (str)(surprice) + "0"
print(surpriceStr)