class Book:
    def __init__(self,page):
          self.page=page
    def __add__(self,other):
        return self.page +other.page
b1=Book(100)
b2=Book(200)
print("total number of pages ",b1+b2)