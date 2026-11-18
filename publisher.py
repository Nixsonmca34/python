class Publisher:
     def __init__(self,name):
        self.name=name

class book(Publisher):
     def __init__(self,name,title,author):
       super().__init__(name)
       self.title=title
       self.author=author

class python(book):
     def __init__(self,name,title,author,price,pages):
       super().__init__(name,title,author)
       self.price=price
       self.pages=pages
       
     def display(self):
         print(self.name)
         print(self.title)
         print(self.author)
         print(self.price)
         print(self.pages)

s1=python("Ram","books","william",300,120)
s1.display()

