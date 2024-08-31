import mysql.connector
from mysql.connector import Error

class DBOperations:

    def connect_database(): # I recommend you replace all inputs here with hard code.
        db_name = input("What is the name of the database you created (see README if you are confused): ")
        user = input("What is the name of the user for your MySQL connection: ")
        password = input("What is the name of the password for your MySQL connection: ")
        host = input("What is the name of the host for your MySQL connection: ")
        
        try:
            connection = mysql.connector.connect(
                database = db_name,
                user = user,
                password = password,
                host = host
                )

            print("Connected to MySQL database successfully.")
            return connection
        
        except Error as e:
            print(f"Error: {e}")
            return None
        
    def disconnect_database(connection):
        if connection is not None:
            
            try:
                connection.close()  
                print("Disconnected from MySQL Database successfully.")

            except Exception as e:
                print(f"Error: {e}")

    def view_user_by_id(connection, name):
        if connection is not None:
            try:
                cursor = connection.cursor()
                
                query = "SELECT * FROM Users WHERE (library_id) = (%s);"
                
                cursor.execute(query, (name,))
                results = cursor.fetchall()
                lib_id = results[0][0]
                name = results[0][1]

                query = "SELECT id, title FROM Books WHERE (borrower_id) = (%s);"
    
                borrowed_books = {}
                cursor.execute(query, (lib_id, ))
                rows = cursor.fetchall()
                
                for row in rows:
                    borrowed_books[row[0]] = row[1]
                
                print(f"Library ID # {lib_id}, Name: {name}, Borrowed Books: {borrowed_books}")

                return True          
                    
            except Exception as e:
                print(f"Error: {e}")
            
            finally:
                cursor.close()

    def display_users_in_db(connection):
        if connection is not None:
            try:
                cursor = connection.cursor()
                
                query = "SELECT * FROM Users;"
                
                cursor.execute(query)
                rows = cursor.fetchall()
                for row in rows:
                    print(f"Library ID # {row[0]}, Name: {row[1]}")
                                    
            except Exception as e:
                print(f"Error: {e}")
                        
            finally:
                cursor.close()

    def log_in_by_id(connection, lib_id):
        if connection is not None:
            try:
                cursor = connection.cursor()

                query = "SELECT * FROM Users WHERE (library_id) = (%s);"
                cursor.execute(query, (lib_id,))
                results = cursor.fetchall()

                if not results:
                    return None
                
                username = results[0][1]
                lib_id = results[0][0]
                        
                query = "SELECT * FROM Books WHERE (borrower_id) = (%s);"
                borrowed_books = []
                cursor.execute(query, (lib_id,))
                rows = cursor.fetchall()

                for row in rows:
                    borrowed_books.append(row[0])

                return (username, borrowed_books, lib_id)

            except Exception as e:
                print(f"Error: {e}")
                return None
            
            finally:
                cursor.close()


    def insert_new_user(connection, user):
        if connection is not None:
            try:
                cursor = connection.cursor()

                query = "INSERT INTO Users (name) VALUES (%s);"

                cursor.execute(query, (user,))
                connection.commit()

                query = "SELECT library_id FROM Users WHERE (name) = (%s)"

                cursor.execute(query, (user,))
                results = cursor.fetchall()
                return results[0][0]


            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()

    def add_author_to_db(connection, author):
        if connection is not None:
            try:
                cursor = connection.cursor()
                
                query = "INSERT INTO Authors (name, bio) VALUES (%s, %s)"
                
                cursor.execute(query, (author.name, author.bio))
                connection.commit()

                query = "SELECT (id) FROM Authors WHERE (name) = (%s) ORDER BY id DESC"

                cursor.execute(query, (author.name,))
                results = cursor.fetchall()
                id = results[0][0]
                return id

            except Exception as e:
                print(f"Error: {e}")
            
            finally:
                cursor.close()

    def display_authors_in_db(connection):
        if connection is not None:
            try:
                cursor = connection.cursor()
                
                query = "SELECT * FROM Authors;"
                
                cursor.execute(query)
                rows = cursor.fetchall()
                for row in rows:
                    print(f"Author ID # {row[0]}, Name: {row[1]}, Bio: {row[2]}")
                
                return ""
            
            except IndexError as ie:
                pass

            except Exception as e:
                print(f"Error: {e}")
                        
            finally:
                cursor.close()


    def view_author_by_id(connection, id):
        if connection is not None:
            try:
                cursor = connection.cursor()
                
                query = "SELECT * FROM Authors WHERE (id) = (%s);"
                
                cursor.execute(query, (id, ))
                results = cursor.fetchall()
                name = results[0][1]
                bio = results[0][2]

                print(f"Author ID # {id}, Name: {name}, Bio: {bio}")          
                    
            except IndexError as ie:
                pass
            
            except Exception as e:
                print(f"Error: {e}")
            
            finally:
                cursor.close()
                return name if results else False

    def add_book_to_db(connection, book):
        if connection is not None:
            try:
                cursor = connection.cursor()
                
                query = "INSERT INTO Books (title, genre, author_id, publication_date, availability) VALUES (%s, %s, %s, %s, %s)"
                
                cursor.execute(query, (book.title, book.genre, book.author_id, book.publication_date, 1))
                connection.commit()
                    
            except Exception as e:
                print(f"Error: {e}")
            
            finally:
                cursor.close()

    def view_book_by_id(connection, id):
        if connection is not None:
            try:
                cursor = connection.cursor()
                
                query = "SELECT * FROM Books WHERE (id) = (%s);"
                
                cursor.execute(query, (id, ))
                results = cursor.fetchall()

                print(f"ID: {results[0][0]}, TITLE: {results[0][1]}, AUTHOR ID: {results[0][2]}, GENRE: {results[0][3]}, PUBLICATION DATE: {results[0][4]}, AVAILABILITY: {results[0][5]}")

            except Exception as e:
                print(f"Error: {e}")
    
    def return_book_by_id(connection, book_id, user):
        if connection is not None:
            try:
                cursor = connection.cursor()

                query = "SELECT * FROM Books WHERE id = %s;"
                cursor.execute(query, (book_id, ))
                results = cursor.fetchall()

                if results:

                    query = "SELECT * FROM Books WHERE id = %s AND borrower_id = %s;"
                    cursor.execute(query, (book_id, user.lib_id))
                    results2 = cursor.fetchall()

                    if results2:

                        query = "UPDATE Books SET availability = %s, borrower_id = %s WHERE id = %s AND borrower_id = %s;"
                        cursor.execute(query, (1, None, book_id, user.lib_id))
                        connection.commit()

                        print(f"Book with id # {book_id} returned.")

                    else:
                        print("Invalid return.")
                
                else:
                    print(f"Book with ID # {book_id} not found in database.")

            except Exception as e:
                print(f"Error: {e}")
            
            finally:
                cursor.close()

    def checkout_book(connection, user, book_id):
        if connection is not None:
            try:
                cursor = connection.cursor()

                query = "SELECT * FROM Books WHERE id = %s;" 
                cursor.execute(query, (book_id,))
                results = cursor.fetchall()

                if results:

                    query = "SELECT * FROM Books WHERE id = %s AND availability = %s;"
                    cursor.execute(query, (book_id, 1))
                    results2 = cursor.fetchall()

                    if results2:

                        query = "UPDATE Books SET availability = %s, borrower_id = %s WHERE id = %s;"
                        cursor.execute(query, (0, user.lib_id, book_id))
                        connection.commit()
                        print(f"Book with ISBN # {book_id} checked out by user with User ID {user.lib_id}.")
                    
                    else: 
                        print(f"Book with ID # {book_id} not available.")
                else:
                    print(f"Book with ID # {book_id} not in records.")

            except Exception as e:
                print(f"Error: {e}")

            finally:
                cursor.close()

    def view_book_by_title(connection, title):
        if connection is not None:
            try:
                cursor = connection.cursor()
                
                query = "SELECT * FROM Books WHERE (title) = (%s);"
                
                cursor.execute(query, (title, ))
                rows = cursor.fetchall()

                if rows:

                    for row in rows:
                        print(f"ID: {row[0]}, TITLE: {row[1]}, AUTHOR ID: {row[2]}, GENRE: {row[3]}, PUBLICATION DATE: {row[4]}, AVAILABILITY: {row[5]}")

                else:
                    print(f"Title {title} not recognized.")

            except Exception as e:
                print(f"Error: {e}")
            
            finally:
                cursor.close()

    def display_books_in_db(connection):
        if connection is not None:
            try:
                cursor = connection.cursor()
                
                query = "SELECT * FROM Books;"
                
                cursor.execute(query)
                rows = cursor.fetchall()
                for row in rows:
                    print(f"ID: {row[0]}, TITLE: {row[1]}, AUTHOR ID: {row[2]}, GENRE: {row[3]}, PUBLICATION DATE: {row[4]}, AVAILABILITY: {row[5]}")
                                    
            except Exception as e:
                print(f"Error: {e}")
                        
            finally:
                cursor.close()