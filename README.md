This Repository is a mini-project for Coding Temple.

## INSTALLATIONS:

```
    git clone https://github.com/gabegoodoi/5_mini_project_library_management_system_with_database_integration/tree/main
```

## SQL TABLES

'''
    
    Use MySQL and create a database with tables that hold the following keys:

    CREATE DATABASE LibraryManagementSystem;

    USE LibraryManagementSystem;

    CREATE TABLE Authors (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        bio TEXT
        );

    CREATE TABLE Users (
        library_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255)
        );

    CREATE TABLE Books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        author_id INT,
        genre VARCHAR(255),
        publication_date YEAR,
        availability BOOL,
        borrower_id INT,
        FOREIGN KEY (author_id) REFERENCES Authors(id),
        FOREIGN KEY (borrower_id) REFERENCES Users(library_id)
        );
'''

## RUN APPLICATION

```
    cd 5_mini_project_library_management_system_with_database_integration
```

From your IDE of choice, select the run button from the main.py file.

## TABLE OF CONTENTS:

1.  main.py
2.  user_interactions.py
3.  book_ops.py
4.  author_ops.py
5.  object_classes.py
6.  error_handling.py
7.  querying.py

---------------------------

1. MAIN.PY

  The application runs through the main.py file. It does so by: 
    
    1st: importing the module from user_interactions.py. 
    2nd: calling the custom method sign_in() from the UserOperations class without any arguments.

---------------------------

2. USER_INTERACTIONS.PY

  The application's UserOperation class methods are defined in this file. In addition, the file imports multiple modules listed below:
  
      1. object_classes.py
      2. error_handling.py
      3. querying.py
      4. book_ops.py
      5. author_ops.py
      6. re
      7. mysql.connector
  
  methods of the UserOperations class:

    1. sign_in()
  
        This method takes no arguments. 
        This method first runs a function to connect to the database then prints a CLI menu directing users to select a path that will allow them to either provide the ID of an existing user, create a new user, or exit the program.

    2. log_in()

        This method takes connection as an argument. 
        It asks users to input an ID and if that ID is in the database it creates a User-object comprised of all that ID's data. 
        It then calls the lib_menu() method with the User-object as an argument. 

    3. sign_up()

        This method takes connection as an argument. 
        It prompts user to input a name and creates a User object with the name as its parameters.
        It then calls the lib_menu() method with the User-object as an argument. 

    4. lib_menu()

        This method takes 2 arguments; a user object and a connection.
        It then prints a CLI menu directing users to select a path that will allow them to access another menu 
        (either: User Operations, Book Operations, or Author Operations)

    5. user_ops_menu()

        This method takes connection as an argument. 
        It then prints a CLI menu directing users to select a path that will allow them to access to either: 
        add a new user, display user details, or display all users

    6. add_user()

        This method takes connection as an argument. 
        It operates much like the sign_up() method with the exception that it does not pass the User-object back to lib_menu(), 
        allowing the user to stay "logged-into" their account while adding a new user to the database.

    
3. BOOK_OPS.PY

  The application's BookOperations class methods are defined in this file.        

  methods of the UserOperations class:

    1. book_ops_menu()
    
        This method takes 2 arguments; a user object and a connection.
        It then prints a CLI menu directing users to select a path that will allow them to activate one of 5 other functions.

    2. add_book()

        This method takes connection as an argument. 
        It asks users to input several variables which it validates. 
        It then creates a Book object using the input variables as arguments. 
        If the author variable is not already in the authors table in the database, it prompts one additional input and creates an Author object. 
        Finally, it adds the book to the Books table of the database..

    3. borrow_book()

        This meethod takes 2 arguments; a user object and a connection.
        This method searches a book id in the Books table, if found and that book's "Available" column value is set to 1, 
        then it's value is changed to 0 and the user's ID is added into the borrower_id value of the Books table entry.

    4. return_book()
    
        This meethod takes 2 arguments; a user object and a connection.
        This method searches a book id in the Books table, if found and that book's "Available" column value is set to 0 and it's borrower matches the user's ID, 
        then it's value is changed to 1 and the user's ID is removed from the borrower_id value of the Books table entry.

    5. find_book()

        This method takes connection as an argument. 
        This method searches a book key in the books dictionary based on the operator's input. It then displays all of that key's values in a formatted manner.

4. AUTHOR_OPS.PY

  The application's AuthorOperations class methods are defined in this file.        

  methods of the UserOperations class:

    1. author_ops_menu()
    
        This method takes connection as an argument. 
        It then prints a CLI menu directing users to select a path that will allow them to activate one of 3 other functions.

    2. add_author()

        This method takes connection as an argument. 
        It asks users to input 2 variables which it validates. 
        It then creates an Author object using the input variables as arguments and adds that author to the database in the Authors table.

    3. view_author_details()

        This method takes connection as an argument. 
        This method searches an author id in the authors table based on the operator's input. It then displays that entry's values in a formatted manner.

    
5. OBJECT_CLASSES.PY

  The application's Author, Book, and User object classes are defined in this file along with their attributes.
  
  Finally, 2 User class methods are defined:
        
    1. get_lib_id()
    
        This method takes no arguments.
        It is a getter that allows operators to access the private self.__lib_id attribute.
        
    2. set_lib_id()

        This method takes self and an ID as arguments (though it defaults the ID to None). 
        It is a setter that allows operators to alter the private self.__lib_id attribute.
  
6. ERROR_HANDLING.PY

  The application's five custom Exception classes are defined in this file. Each of these classes inherits the Exception class.

      1. NameError
      2. CommaError
      3. DuplicateError
      4. YearError
      5. LengthError
  
7. QUERYING.PY

  This file contains the SQL querying logic and functions.


      1. connect_database(): connects to the database and gives the rest of the program access to the data.
      2. disconnect_database(): disconnects from the database when users exit from the program.
      3. view_user_by_id(): selects and displays data from the Users table by ID input.
      4. display_users_in_db(): displays all data in users table
      5. log_in_by_id(): selects and returns values of user to create User object from the Users table by ID input.
      6. insert_new_user(): Inserts values of new user entry in Users table.
      7. add_author_to_db(): Inserts values of new author entry in Authors table.
      8. display_authors_in_db(): displays all data in authors table
      9. view_author_by_id(): selects and displays data from the Authors table by ID input.
      10. add_book_to_db(): Inserts values of new book entry in Books table.
      11. view_book_by_id(): selects and displays data from the Books table by ID input.
      12. return_book_by_id(): Updates values of book entry in books table to specify availability and borrower.
      13. checkout_bok(): Updates values of book entry in books table to specify availability and borrower.
      14. view_book_by_title(): selects and displays data from the Books table by title input.
      15. display_books_in_db(): displays all data in Books table