class Book:
    def __init__(self, title, author_id, genre, publication_date, availability="Available"):
        self.title = title
        self.author_id = author_id
        self.genre = genre
        self.publication_date = publication_date
        self.availability = availability

class User:
    def __init__(self, name, lib_id, borrowed_books=None):
        self.name = name
        self.__lib_id = lib_id
        self.borrowed_books = borrowed_books if borrowed_books is not None else []

    def get_lib_id(self):
        return self.__lib_id

    def set_lib_id(self, new_id=None):
        self.__lib_id = new_id

class Author:
    def __init__(self, name, bio=None):
        self.name = name
        self.bio = bio
