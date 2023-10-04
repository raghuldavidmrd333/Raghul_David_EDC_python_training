class Node:
    def __init__(self, value,_next=None, previous=None):
        self._value=value
        self._next=_next
        self._previous=previous

class LinkedList:
    def __init__(self):
        self._first=None
        self._last=None

    def append(self, value):
        if self._first==None: 
            NN = Node(value)
            self._first=NN
            self._last=NN
        else: 
            n=self._first
            while n._next:
                n=n._next
            NN=Node(value, previous=n)
            n._next=NN
            self._last=NN

    def get_first(self):
        first = self._first._value if self._first else None
        print("FIRST :",first)

    def get_last(self):
        last = self._last._value if self._last else None
        print("LAST :", last)

    def remove(self):
        self._first = None
        self._last = None

    def append_last(self,value):
        if self._first==None: 
            NN = Node(value)
            self._first=NN
            self._last=NN
        else: 
            NN=Node(value,previous=self._last)
            self._last._next=NN
            self._last=NN
            print(self._last._value)

    def info(self):
        if self._first==None: 
            return "LinkedList(empty)"
        str="LinkedList(\t"
        n=self._first
        while n:
            str+=f'{n._value}\t'
            n=n._next
        str+=")"
        return str
    
    
    def count(self, value):
        current = self._first 
        count = 0
        while(current != None):
            if(current._value == value):
                count += 1
            current = current._next
        return count





    def size(self):
        c=0
        n=self._first
        while n:
            c+=1
            n=n._next
        return c
LL = LinkedList()

print(LL.info())

for i in [9,8,7,1,3,2,4,5,6]:
    LL.append(i)

print("the siz of this list is :" ,LL.size())
print()
print("the last value in this list is\n",LL._last._value)
print()
LL.append_last(20)
print(LL.info())

def get(list,index):
    n=list._first
    for i in range(index):
        n=n._next
        if n==None:
            break
    else:
        return n._value

LinkedList.get = get

LL.get(5)

def set(list,index,value):
    n=list._first
    for i in range(index):
        n=n._next
        if n==None:
            break
    else:
        n._value=value

LinkedList.set=set

LL2=LinkedList()
for i in range(5):
    LL2.append(i)
    
for i in range(LL2.size()):
    print(LL2.get(i))
    LL2.set(i, i*10)

print(LL2.info())

def loop(list,index):
    count = 0
    prev = list._first
    cur = list._first
    while count<index and cur:
        prev = cur            
        cur = cur. _next                
        count+=1
    return [prev,cur]

def insert(list, index, value):
    if (index > list.size()) or index<0:
        print("Invalid INdex")

    else:
    
        if index == 0:
            NN2 = Node(value,list._first,None)
            list._prev = NN2
            list._first = NN2


        else:
            prev,cur = loop(list,index)
            print(prev._value)
            if index == list.size():
                NN2 = Node(value,None,prev)
                prev. _next = NN2
            else:
                NN2 = Node(value,cur,prev)
                cur._previous = NN2
                prev. _next = NN2

        
    

def remove(list, index):
    if (index > list.size()) or index<0:
        print("Invalid INdex")

    else:
    
        if index == 0:
            list._first = list._first. _next
            list._first._previous = None


        else:
            prev,cur = loop(list,index)
            print(cur._value)
            print(prev._value)
            if index == list.size()-1:
                 prev. _next = None
            else:
                  prev. _next = cur. _next
                  cur. _next._prev = prev
remove(LL2,6)
print(LL2.info())
