def abc(l):
    d={}
    for i in range(len(l)):
        a=l[i]
        count=0
        for j in range(i,len(l)):
            if l[j]==l[i]:  
                count=count+1
        m=f'{count * "[][][][]"} {count}'
        c=dict({a:m})
        
        if a not in d.keys():
            d.update(c)
    for x,y in d.items():
        print(x,y)
    print(d)

abc([1,1,1,2,2,3,3,3,3,3,3,1,1,3,3,3,2])