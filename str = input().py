str = input()
new = ""
for i in str:
    if i in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
        new = new + i + " "
print(new)