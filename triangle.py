class triangle():
    def perimeter(self,s1,s2,s3):
        p=s1+s2+s3
        
        print("the perimeter of a triangle is : ",p)
    
obj1=triangle()


class circle():
    def perimeter(self,r):
        p=2*3.14*r
        
        print("the perimeter of a circle is : ",p)
obj2=circle()

obj1.perimeter(3,4,5)
obj2.perimeter(4)

    