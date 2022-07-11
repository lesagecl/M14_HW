import numpy as np
import pandas as pd

# Name: Chelsea Le Sage
# User ID: cl5bd
class BookLover:
    
    num_books = 0
    book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    
    # Constructor
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
    
    def add_book(self, book_name, book_rating):
        if self.book_list[self.book_list['book_name'] == book_name].any().any():
            print('Book already in list')
        else:
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [book_rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
            print('Book added to list')
    
    def has_read(self, book_name):
        return self.book_list[self.book_list['book_name'] == book_name].any().any()
    
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]