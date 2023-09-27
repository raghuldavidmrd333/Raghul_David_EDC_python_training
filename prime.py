min = int(input("Enter the min value: "))

max = int(input("Enter the max value: "))

print("the prime numbers between",min,"and"," " ,max,"are",":",end=" ")

for n in range(min, max+1):

    if n>1:
        m=int(n/2)
        for i in range(2,m):

            if (n%i)==0:

                break

        else:
            print(n,end="\t")