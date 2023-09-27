from math import sqrt

class Circle:
    pass
    
def create(r):
    c=Circle()
    c.r=r
    return c
    
def perimeter(c):
    return 2*(22/7)*c.r

def area(c):
    return (22/7)*c.r*c.r

def info(c):
     return f'Circle :  radius : {c.r}'

def draw(c):
    print(info(c))
    
def result_circle(r):
    c=create(r)

    print("area :",area(c))
    print("perimeter :",perimeter(c))
    
    
result_circle(3)