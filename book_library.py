class Book:
  def __init__(self, name, author, copies):
      self.name = name
      self.author = author
      self.copies = copies

  def __str__(self):
      return " Book:" +self.name + \
             " Author:" + self.author + \
             " Copies Available:"+str(self.copies) 


class Library:
  def __init__(self):
      self.books = [] 

  def add_book(self, name, author, copies):

      for book in self.books:
          if book.name.lower() == name.lower() and book.author.lower() == author.lower():
              book.copies += copies
              print(" Added ",book.copies, "more copies of", book.name)
              return

      new_book = Book(name, author, copies)
      self.books.append(new_book)
      print(" Book", new_book.name," by" ,new_book.author," added with", new_book.copies,    
            "copies.")

  def delete_book(self, name, author):
      for book in self.books:
          if book.name.lower() == name.lower() and book.author.lower() == author.lower():
              self.books.remove(book)
              print(" Book", book.name, "by", book.author, "removed from the library.")
              return
      print(" Book", book.name, "by", book.author, "not found in the library.")

  def search_book(self, name):
      for book in self.books:
          if book.name.lower() == name.lower():
              print(book)
              return
      print(" Book", book.name, "not found in the library.")

  def allocate_book(self, name):
      for book in self.books:
          if book.name.lower() == name.lower():
              if book.copies > 0:
                  book.copies -= 1
                  print(" Book:", book.name, "has been allocated.Copies left:",book.copies)
              else:
                  print(" Book", book.name, "is currently out of stock.")
              return
      print(" Book" ,book.name," not found in the library.")

  def deallocate_book(self, name):
      for book in self.books:
          if book.name.lower() == name.lower():
              book.copies += 1
              print(" Book:",book.name, "has been returned. Copies available:",book.copies)
              return
      print(" Book", book.name, "not found in the library.")

  def show_books(self):
      if not self.books:
          print("No books are currently available in the library.")
      else:
          print("\nBooks in the Library:")
          for book in self.books:
              print(book)


library = Library()
library.add_book("Python Programming", "A.D", 5)
library.add_book("Data Structures", "K.B", 3)
library.show_books()
library.search_book("Python Programming")
library.allocate_book("Python Programming")
library.show_books()
library.deallocate_book("Python Programming")
library.delete_book("Data Structures", "K.B")
library.show_books()
