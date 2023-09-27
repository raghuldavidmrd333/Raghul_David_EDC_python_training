def frequency_distribution(*args,design,show,align):
    d={}
    for i in range(len(args)):
        a=args[i]
        count=0
        for j in range(i,len(args)):
            if args[j]==args[i]:
                count=count+1
        if show:
            
            h=f'{count * design}{count}'
            c=dict({a:h})
            if a not in d.keys():
                d.update(c)
        else:
            h=f'{count * design}'
            c=dict({a:h})
            if a not in d.keys():
                d.update(c)
            
        

    print("The frequency distribution is ")
    
    
    if(align):
        for x,y in d.items():
            space=' '*(50-len(y))
            lenres=len(y)//6
            res=f'{x}{" "}{y}{space}{lenres}'

            
            print(res)
    else:
        for x,y in d.items():
            print(x,y)
           
    #print (d)


#l=list(map(int,input().split()))
frequency_distribution(1,2,3,4,5,4,3,3,3,3,3,3,3,3,3,3,3,3,3,2,1,5,2,3,3,1,2,3,4,6,design="++++  ",show=False,align=True)

