def count_of_ele(l):
    d={}
    for i in range(len(l)):
        a=l[i]
        count=0
        for j in range(i,len(l)):
            if l[j]==l[i]:
                count=count+1
        
        c=dict({a:count})
        if a not in d.keys():
            d.update(c)
    print("the count of each element is")        
    print (d)

l=list(map(int,input().split()))
count_of_ele(l)

