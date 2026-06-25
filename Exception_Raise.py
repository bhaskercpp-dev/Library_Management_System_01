class Book:
    def __int__(self,title,auther,isbn):
        self.title = title
        self.auther = auther
        self.isbn = isbn
    def __str__(self):
        return f"Title: {self.title} ,Auther : {self.auther},ISBN : {self.isbn}"
    
class Library:

    def __init__(self):
        self.books = []

    def Add_Book(self,book):
        self.books.append(book)
        return f"Book {book.title} added to the Library"

    def Remove_Book(self,isbn):
        for book in self.books:
            if self.books.isbn == isbn:
                self.books.remove(book)
                print(f"Book {book.title} removed from the Library")
            else:
                print("Book Not Found")
    def Search_Book(self,title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            print("Search Found")
            for book in found_books:
                print(book)
        else:
            print("No Books Found")
    def list_books(self):
        if self.books:
            print("Library Catalog:")
            for book in self.books:
                print(book)
        else:
            print("No books in the library.")

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. List all books")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            book = Book(title, author, isbn)
            library.add_book(book)
        elif choice == '2':
            isbn = input("Enter the ISBN of the book to remove: ")
            library.remove_book(isbn)
        elif choice == '3':
            title = input("Enter the title to search for: ")
            library.search_book(title)
        elif choice == '4':
            library.list_books()
        elif choice == '5':
            print("Exiting the library management system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()                                                        