class Book:
  # definiendo el constructor
  def __init__(self, title, author, year, isbn):
    self.title = title
    self.author = author
    self.year = year
    self.isbn = isbn

books = [
  Book("Odyssey", "Homer", -750, 1234567890123),
  Book("Iliad", "Homer", -750, 1234567890124),
  Book("Harry Potter", "Jk Rowling", 1999, 1234567890125),
  Book("Harry Potter 2", "Jk Rowling", 1999, 1234567890126),
]

while True:
  print("")
  print("MENU")
  print("1. Add book")
  print("2. Show all books")
  print("0. EXIT")

  option = int(input("Type selection:"))

  match option:
    case 1:
      print("")
      print("ADD BOOK")
      title = input("Insert book title: ")
      author = input("Insert book author: ")
      year = int(input("Insert book publication year: "))
      isbn = int(input("Insert books ISBN: "))

      books.append(
        # llamar al constructor
        Book(
          title, author, year, isbn
        )
      )

      print("Book added...")

    case 2:
      print("")
      print("-- ALL BOOKS --")

      for i in range(len(books)):
        print(books[i].isbn, books[i].title, books[i].author, books[i].year)
