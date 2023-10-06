import time

def performance_log(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"The Function {func.__name__} took {execution_time:.3f} seconds to complete the task.")
    return result

  wrapper.time_taken = -1
  return wrapper

@performance_log
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

primes = find_primes(2, 50000)
print("the total primes between the range is ",len(primes))