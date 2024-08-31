from object_classes import *
from error_handling import *
from querying import *
import re

class AuthorOperations:
    def author_ops_menu(connection):
        print("\nWelcome to the Author Operations Menu!")
        while True:
            selection = input("\nMain Menu:\n1. Add a new author\n2. View author details\n3. Display all authors\n4. Quit\n")
            if selection == '1':
                AuthorOperations.add_author(connection)
            elif selection == '2':
                AuthorOperations.view_author_details(connection)
            elif selection == '3':
                DBOperations.display_authors_in_db(connection)
            elif selection == '4':
                print("\nReturning to Library Management System!")
                break
            else:
                print("\nInvalid Input: must be 1-4. Try again.")

    def add_author(connection):
        author_name = input("Please enter the author's name: ")
        try:
            if len(author_name) < 1:
                raise LengthError
            elif not re.match(r"^[A-Za-z \.'-]+$", author_name):
                raise NameError  
        except LengthError as le:
            print("LENGTH ERROR: Input must be at least 1 character in length.")
        except NameError as error:
            print("NAME ERROR: Input must not include punctuation, numbers, symbols, or letters not contained in the English alphabet (exception: apostrophe, period, dash).")
        else:
            bio = input(f"Please enter a biographical blurb for {author_name}: ")
            author = Author(author_name, bio)
            DBOperations.add_author_to_db(connection, author)
            print(f"{author.name} added to the database")

    def view_author_details(connection):
        author_id = input("Please enter the the author's ID: ")
        found = False
        if DBOperations.view_author_by_id(connection, author_id):
            found = True
        elif not found:
            print(f"{author_id} not found in library records.")