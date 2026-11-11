day = input()
ticket = int(input())
price = ticket*200
if day == "Monday":
    if ticket>4:
        price = price - 150

print("Total amount to be paid:",price)