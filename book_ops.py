from object_classes import *
from error_handling import *
from querying import *
import re

class BookOperations:
    def book_ops_menu(user, connection):
        print("\nWelcome to the Book Operations Menu!")
        while True:
            selection = input("\nMain Menu:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books\n6. Quit\n")
            if selection == '1':
                BookOperations.add_book(connection)
            elif selection == '2':
                BookOperations.borrow_book(user, connection)
            elif selection == '3':
                BookOperations.return_book(user, connection)
            elif selection == '4':
                BookOperations.find_book(connection)
            elif selection == '5':
                DBOperations.display_books_in_db(connection)
            elif selection == '6':
                print("\nReturning to Library Management System!")
                break
            else:
                print("\nInvalid Input: must be 1-6. Try again.")

    def add_book(connection):
            title = input("Please enter the title of the book: ")
            try:
                if len(title) < 1:
                    raise LengthError 
            except LengthError as le:
                print("LENGTH ERROR: Input must be at least 1 character in length.")
            else:
                genre = input(f"Please enter the genre of {title}: ")
                try:
                    if len(genre) < 1:
                        raise LengthError 
                except LengthError as le:
                    print("LENGTH ERROR: Input must be at least 1 character in length.")
                else:
                    print(f"\nPlease enter the ID of the author of {title} from the following authors, if your author is not listed press RETURN:\n")
                    author_id = input(f"\n{DBOperations.display_authors_in_db(connection)}")                   
                    match  = DBOperations.view_author_by_id(connection, author_id)

                    if not match:
                        name = input(f"Please enter the name of the author of {title}: ")
                        bio = input(f"Thank you for adding a book by a new author to the library, Please enter a biographical blurb for {name}: ")
                        author = Author(name, bio)
                        author_id = DBOperations.add_author_to_db(connection, author)

                    pub_date = input(f"Please enter the publication year of {title}: ")
                    try:
                        if not re.match(r"^[0-9]{4}$", pub_date):
                            raise YearError
                    except YearError as ye:
                        print("YEAR ERROR: Input must be exactly 4 numerical characters (0-9).")
                    else:
                        book = Book(title, author_id, genre, pub_date)
                        DBOperations.add_book_to_db(connection, book)
                        print(f"{title} added to library.")

    def borrow_book(user, connection):
        book_id = input("Please enter the ID # of the book you'd like to borrow: ")
        availability = DBOperations.view_book_by_id(connection, book_id)
        if availability != 0:
            DBOperations.checkout_book(connection, user, book_id)
        else:
            print(f"{book_id} not available.")
    
    def return_book(user, connection):
        book_id = int(input("Please enter the ID # of the book you'd like to return: "))
        DBOperations.return_book_by_id(connection, book_id, user)

    def find_book(connection):
        title = input("Please enter the title of the book you'd like to find: ")
        DBOperations.view_book_by_title(connection, title)