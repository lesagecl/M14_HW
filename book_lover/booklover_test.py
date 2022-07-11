from booklover import BookLover
import unittest

class BookLoverTestSuite(unittest.TestCase):
    
    # add a book and test if it is in `book_list`.
    def test_1_add_book(self):
        user = BookLover("Jasmine", "jmalek@virginia.edu", "mystery")
        user.add_book("The Guest List", 4)
        self.assertEqual(True, user.book_list[user.book_list['book_name'] == "The Guest List"].any().any())
        
    # add the same book twice. Test if it's in `book_list` only once
    def test_2_add_book(self):
        user = BookLover("Gunnar", "gfranko@virginia.edu", "educational")
        user.add_book("Webster's Dictionary", 4)
        user.add_book("Webster's Dictionary", 4)
        self.assertEqual(1, user.num_books_read())
        user.add_book("The Magic Treehouse", 5)
        self.assertEqual(2, user.num_books_read())
    
    # pass a book in the list and test if the answer is `True`.
    def test_3_has_read(self):
        user = BookLover("Rory", "rblack@virginia.edu", "romance")
        user.add_book("Twilight", 5)
        user.add_book("New Moon", 4)
        self.assertEqual(True, user.has_read("Twilight"))
        self.assertTrue(user.has_read("New Moon"))
        self.assertEqual(False, user.has_read("Breaking Dawn"))
    
    # pass a book NOT in the list and use `assert False` to test the answer is `True`
    def test_4_has_read(self):
        user = BookLover("Chelsea", "clesage@virginia.edu", "fiction")
        self.assertFalse(user.has_read("Memoirs of a Geisha"))
        
    # add some books to the list, and test num_books matches expected
    def test_5_num_books_read(self):
        user = BookLover("Julia", "jburek@virginia.edu", "non-fiction")
        user.add_book("My Side of the Mountain", 3)
        user.add_book("The Declarattion of Independence", 4)
        user.add_book("The Constitution", 1)
        self.assertEqual(3, user.num_books_read())
    
    # add some books with ratings to the list, making sure some of them have rating > 3. 
    # Your test should check that the returned books have rating  > 3
    def test_6_fav_books(self):
        user = BookLover("Bella", "bsampler@virginia.edu", "fiction")
        user.add_book("Convenience Store Woman", 2)
        user.add_book("If I Had Your Face", 4)
        user.add_book("The Goldfinch", 5)
        user.add_book("Clara and The Sun", 3)
        user.add_book("The Ladies of Grace Adieu", 4)
        df = user.fav_books()
        print(df.head())

if __name__ == '__main__':
    unittest.main(verbosity=3)