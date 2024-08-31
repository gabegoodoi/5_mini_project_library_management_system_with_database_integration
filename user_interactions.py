from querying import *
import mysql.connector
from mysql.connector import Error
from object_classes import *
from error_handling import *
from book_ops import *
from author_ops import *
import re

class UserOperations:
    def sign_in():
        connection = DBOperations.connect_database()
        while True:
            selection = input("\nWelcome to the Sign In page!\n1. Log in to existing account\n2. Create new account\n3. Quit\n")
            if selection == '1':
                UserOperations.log_in(connection)
            elif selection == '2':
                UserOperations.sign_up(connection)
            elif selection == '3':
                DBOperations.disconnect_database(connection)
                break
            else:
                print("\nInvalid Input: must be 1-3. Try again.")

    def log_in(connection):
        lib_id = input("Please enter user ID: ")
        try:
            result = DBOperations.log_in_by_id(connection, lib_id)

            if result is None:
                print("User ID not found in the database")
                return
            
            username, borrowed_books, lib_id = result

            print(f"Hello again, {username}")
            user_object = User(username, lib_id, borrowed_books)
            
            UserOperations.lib_menu(user_object, connection)

        except Exception as e:
            print(f"ERROR: {e}")

    def sign_up(connection):
        username = input("Creating account. Please provide your name: ")
        try:
            if len(username) < 1:
                raise LengthError             
        except LengthError as le:
            print("LENGTH ERROR: Input must be at least 1 character in length.")        
        else:
            lib_id = DBOperations.insert_new_user(connection, username)
            user = User(username, lib_id)
            print(f"Account successfully created with following details.\nLibrary ID ----- {lib_id}\nName ----------- {user.name}\n")
            UserOperations.lib_menu(user, connection)

    def lib_menu(user, connection):
        print("\nWelcome to the Library Management System!")
        while True:
            selection = input("\nMain Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit\n")
            if selection == '1':
                BookOperations.book_ops_menu(user, connection)
            elif selection == '2':
                UserOperations.user_ops_menu(connection)
            elif selection == '3':
                AuthorOperations.author_ops_menu(connection)
            elif selection == '4':
                break
            else:
                print("\nInvalid Input: must be 1-4. Try again.")

    def user_ops_menu(connection):
        print("\nWelcome to the User Operations Menu!")
        while True:
            selection = input("\nMain Menu:\n1. Add a new user\n2. View user details\n3. Display all users\n4. Quit\n")
            if selection == '1':
                UserOperations.add_user(connection)
            elif selection == '2':
                UserOperations.view_user_details(connection)
            elif selection == '3':
                DBOperations.display_users_in_db(connection)
            elif selection == '4':
                print("\nExiting User Operations menu.")
                break
            else:
                print("\nInvalid Input: must be 1-4. Try again.")

    def add_user(connection):
        new_username = input("Please provide new user's name: ")
        try:

            if len(new_username) < 1:
                raise LengthError   
                      
        except LengthError as le:
            print("LENGTH ERROR: Input must be at least 1 character in length.")      

        else:
            lib_id = DBOperations.insert_new_user(connection, new_username)
            new_user = User(new_username, lib_id)
            print(f"{new_username} added to databasewith Library ID # {lib_id}.")

    def view_user_details(connection):
        user_id = int(input("Please enter user ID: "))
        found = DBOperations.view_user_by_id(connection, user_id)
        if found is None:
            print(f"{user_id} not found in library records.")        


