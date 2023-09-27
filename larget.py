s=input("enter the numbers :").split()
max = s[0]
for x in s:
    if x > max:
        max = x
print("The greates number is:",max)