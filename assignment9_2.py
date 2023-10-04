class Book:
    def __init__(self,id,title,author,price,rating):
        self.id=id
        self.title=title
        self.author=author
        self.price=price 
        self.rating=rating
class library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
    def Find_by_ID(self,ID):
        for book in self.books:
            if book.id==ID:
                print(f"{book.id},{book.title},{book.author},{book.price},{book.rating}")
        return None
    def Find_by_author(self,author_name):
        for book in self.books:
            if book.author==author_name:
                print(f"{book.id},{book.title},{book.author},{book.price},{book.rating}")
        return None
    def Find_by_rating(self,start,end):
        for book in self.books:
            if (book.rating>start and book.rating<end):
                print(f"{book.id},{book.title},{book.author},{book.price},{book.rating}")
        return None
    def Find_by_price(self,start,end):
        for book in self.books:
            if (book.price>start and book.price<end):
                print(f"{book.id},{book.title},{book.author},{book.price},{book.rating}")
        return None
    def info(self):
        for i in self.books:
            print(f"{i.id},{i.title},{i.author},{i.price},{i.rating}")

b1=Book(1111,"chronicles of narnia","MRD",2000,8)
b2=Book(2222,"harrypotter","Raghul",320,7)
b3=Book(3333,"marvel","SAI",725,6)
b4=Book(4444,"GOT","PRAVEEN",2000,10)
l=library()
l.add_book(b1)
print()
l.add_book(b2)
l.add_book(b3)
l.add_book(b4)
print("Books list:")
print()
l.info()
print("finding book by id=2222:")
print()
l.Find_by_ID(2222)
print("finding book by author=MRD:")
print()
l.Find_by_author("MRD")
print("finding books by rating between 3 and 5")
print()
l.Find_by_rating(3,5)
print("finding book by price between 320 and 1000")
print()
l.Find_by_price(320,1000)
