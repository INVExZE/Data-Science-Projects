'''Write a Library class with no_of_books and books 
as two instance variables. Write a program to create 
a library from this Library class and show how you 
can print all books, add a book and get the number of 
books using different methods. Show that your program 
doesnt persist the books after the program is stopped!'''


class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def info(self):
        print(f"The Library has {self.noBooks} Books.\nThe List of All Books are : ")
        for book in self.books:
            print(book)

l1 = Library()
l1.addBook('"The Indian History"')
l1.addBook('"The Indian Movie"')
l1.addBook('"The Indian Music"')
l1.addBook('"The Indian Match"')
l1.addBook('"The Indian Show"')
l1.addBook('"The Indian Food"')
l1.addBook('"The Indian Place"')
l1.addBook('"The Indian Tea"')
l1.addBook('"The Indian Road"')
l1.addBook('"The Indian Sea"')
l1.info()


        
