class Node:
    def _init_(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

class PrimeRangeIterator:
    def _init_(self, start, end=None):
        self.linked_list = LinkedList()
        self.linked_list.append(Node(start))
        self.current = self.linked_list.head
        self.end = end

    def _iter_(self):
        return self

    def _next_(self):
        while self.current is not None:
            if self.is_prime(self.current.value):
                return self.current.value
            self.current = self.current.next
        raise StopIteration()

    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

def prime_range(start, end=None):
    return PrimeRangeIterator(start, end)

print('\n')
try:
    primes = prime_range(10, 20)
    it = iter(primes)
    for i in range(5):
        print(next(it))
except StopIteration:
    pass