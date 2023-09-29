class Node:

    def __init__(self, data):

        self.data = data

        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None

    def append(self, new_data):

        new_node = Node(new_data)

        if self.head is None:

            self.head = new_node

            return

        last = self.head

        while (last.next):

            last = last.next

        last.next = new_node

    def insert(self, x, new_data):

        current=self.head

        new_node=Node(new_data)

        if current is None:

            self.head=new_node

            return

        i=1

        while current != None:

            if i== x:

                break

            i+=1

            current=current.next

        new_node.next = current.next

        current.next = new_node

    def get(self, x):

        current = self.head

        i=0

        while current != None:

            if i== x:

                return current.data

            i+=1

            current=current.next

    def set(self,x,value):

        current = self.head

        i=0

        while current != None:

            if i== x:

                current.data=value

                break

            i+=1

            current=current.next


    def size(self):

        current=self.head

        count=0

        while current!=None:

            count+=1

            current=current.next

        return count

    def info(self):

        if(self.head==None):

            print("list is empty")

            return

        current=self.head

        while(current.next!=None):

            print(current.data,end="->")

            current=current.next

        print(current.data)

    def remove(self,x):

        current=self.head

        prev=self.head

        if(current.next==None):

            val=current.data

            self.head=None

            return val

        current=current.next

        i=1

        while(current!=None):

            if(i==x):

                val=current.data

                prev.next=current.next

                return val

            i+=1

            prev=current

            current=current.next

    def clear(self):

        self.head=None


li=LinkedList()

li.append(1)

li.append(2)

li.append(3)

li.insert(1,5)

print("after inserting 5 at 1st index ",end=" ")

li.info()

print("getting value at 1 st index->",li.get(1))

li.set(0,6)

print("list after changing 0 index to 6 ",end=" ")

li.info()

print("size=",li.size())

print("removed data value is ",li.remove(2))

print("list after removing 2 nd index ",end=" ")

li.info()

li.clear()

li.info()