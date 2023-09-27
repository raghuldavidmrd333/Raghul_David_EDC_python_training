s=input("enter the numbers :").split()
max = s[0]
max1=s[0]
for x in s:
    if max < x:
        max1=max
        max=x
        
print("second largest is ",max1)





