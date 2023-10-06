import time
from contextlib import contextmanager

class Timer:
    def _init_(self):
        self.start_time = time.time()

    def _enter_(self):
        return self

    def _exit_(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        self.time_taken = self.end_time - self.start_time

def find_primes(min, max):
  primes = []
  for i in range(min, max + 1):
    if is_prime(i):
      primes.append(i)
  return primes

def is_prime(n):
  m=int(n/2)
  for i in range(2, m + 1):
    if n % i == 0:
      return False
  return True

with Timer() as t:
    primes = find_primes(2, 20000)
    print('total primes in the given range is : ', len(primes))

print('total time taken for executingnthis task is :', t.time_taken)