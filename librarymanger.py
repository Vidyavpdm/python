
        

from book import Book

class LibraryManager:
    def __init__(self):
        self.books = []
        self.borrowed_books = {}
        self.registered_users = {} 
        
    def add_book(self, book_object):
        self.books.append(book_object)
        
    def delete_book_by_name(self, book_name):
        for book in self.books:
            if book.name == book_name:
                self.books.remove(book)
                return True
        return False
        
    def get_book_by_name(self, book_name):
        for book in self.books:
            if book.name == book_name:
                print(f"Book '{book_name}' found in LibraryManager.")
                return book
        print(f"Book '{book_name}' not found in LibraryManager.")
        return None

    def list_books(self):
        print("Books in LibraryManager:")
        for book in self.books:
            print(book.name)
    def is_book_available(self, book_isbn):
        return book_isbn not in self.borrowed_books
    def is_user_registered(self, person_id):
        return person_id in self.registered_users
    def assign_book_to_user(self, book_isbn, person_id):
            
        if person_id not in self.registered_users:
            print(f"User with ID '{person_id}' is not registered. Please register first.")
            return
        
        book = self.get_book_by_isbn(book_isbn)
        if not book:
            print(f"Book with ISBN '{book_isbn}' not found in LibraryManager.")
        elif book_isbn in self.borrowed_books:
            print(f"Book with ISBN '{book_isbn}' is already borrowed by someone.")
        else:
            self.borrowed_books[book_isbn] = person_id
            print(f"Book with ISBN '{book_isbn}' has been assigned to person with ID '{person_id}'.")

   

 






    def get_book_by_isbn(self, book_isbn):
        for book in self.books:
            if book.ISBN == book_isbn:
                return book
        return None

    '''def list_taken_books(self, book_isbn):
        if book_isbn in self.borrowed_books:
            person_id = self.borrowed_books[book_isbn]
            print(f"Book with ISBN '{book_isbn}' is assigned to person with ID '{person_id}'.")
        else:
            print(f"Book with ISBN '{book_isbn}' is not currently assigned to anyone.")'''

    def list_all_books_details(self):
        print("Details of all books in LibraryManager:")
        for book in self.books:
            status = "Assigned" if book.ISBN in self.borrowed_books else "Available"
            print(f"- Book Name: {book.name}, ISBN: {book.ISBN}, Status: {status}")

    '''def list_all_books_status(self):
        print("Status of all books in LibraryManager:")
        for book in self.books:
            status = "Assigned" if book.ISBN in self.borrowed_books else "Available"
            print(f"- Book Name: {book.name}, Status: {status}")'''

    def register(self, name, user_id, password):
            if user_id in self.registered_users:
                print("User with this ID is already registered. Please choose a different user ID.")
            else:
                self.registered_users[user_id] = password
                print(f"Hello {name}, you are successfully registered in the library!!..")
lm = LibraryManager()
name = input("Enter your name here!!: ")
user_id = input("Enter your user ID: ")
password = input("Enter your password: ")
lm.register(name, user_id, password)

#  Book objects
book1 = Book("DO EPIC SHIT", "78463738")
book2 = Book("Python 101", "94857392")
book3= Book("True love","564738920")

# Add books 
lm.add_book(book1)
lm.add_book(book2)
lm.add_book(book3)


isbn_to_assign = input("Enter the ISBN of the book to assign: ")
assign_to_user_id = input("Enter the user ID to assign the book: ")

if lm.is_book_available(isbn_to_assign):
    if lm.is_user_registered(assign_to_user_id):
        lm.assign_book_to_user(isbn_to_assign, assign_to_user_id)
    else:
        print(f"User with ID '{assign_to_user_id}' is not registered. Please register first.",)
else:
    print(f"Book with ISBN '{isbn_to_assign}' is not available for assignment.")
# List all books


# Get book by name
searched_book_name = input("Enter the book name that you need to assign: ")
lm.get_book_by_name(searched_book_name)
lm.list_all_books_details()


# Delete a book by name
book_to_delete = input("Enter the book that needs to be deleted: ")
if lm.delete_book_by_name(book_to_delete):
    print(f"Book '{book_to_delete}' deleted.")
else:
    print(f"Book '{book_to_delete}' not found, cannot delete.")
lm.list_books()

