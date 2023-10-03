class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self,data):
        newN = Node(data)
        if self.head==None:
            self.tail = newN
            self.head = newN
        else:
            self.tail.next = newN
            self.tail = newN
        self.size+=1

    def info(self):
            cur = self.head
            for i in range(self.size-1):
                print(f'{cur.data}->',end="")
                cur = cur.next
            print("None")


    

    def is_prime(self, num):
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True

    def print_primes(self):
            current = self.head
            while current:
                if self.is_prime(current.data):
                    print(current.data, end=" ")
                current = current.next

    def is_even(self,num):
         if num %2 ==0:
            return True
    def print_even(self):
            current = self.head
            while current:
                if self.is_even(current.data):
                    print(current.data, end=" ")
                current = current.next
    

ll=LinkedList()
for i in range(20):

    ll.append(i+1)

ll.info()
print("Prime numbers in the linked list : \n")
ll.print_primes()
print()
print()
print("Even numbers in the linked list : ")

ll.print_even()