import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        # Add a book and test if it is in book_list.
        book_lover = BookLover("John Doe", "john@gmail.com", "mystery")
        book_lover.add_book("The Girl with the Dragon Tattoo", 5)
        self.assertTrue(book_lover.has_read("The Girl with the Dragon Tattoo"))

    def test_2_add_book(self):
        # Add the same book twice. Test if it's in book_list only once.
        book_lover = BookLover("Jane Smith", "jane@gmail.com", "fantasy")
        book_lover.add_book("Harry Potter and the Sorcerer's Stone", 4)
        book_lover.add_book("Harry Potter and the Goblet of Fire", 3)
        self.assertEqual(book_lover.num_books_read(), 2) 


    def test_3_has_read(self):
        # Pass a book in the list and test if the answer is True.
        book_lover = BookLover("Alice Johnson", "alice@gmail.com", "sci-fi")
        book_lover.add_book("Dune", 5)
        self.assertTrue(book_lover.has_read("Dune"))

    def test_4_has_read(self):
        # Pass a book NOT in the list and use assert False to test if the answer is False.
        book_lover = BookLover("Bob Wilson", "bob@gmail.com", "thriller")
        book_lover.add_book("The Lord of the Rings: The Fellowship of the Ring", 3)
        self.assertFalse(book_lover.has_read("Harry Potter and the Chamber of Secrets"))

    def test_5_num_books_read(self):
        # Add some books to the list, and test num_books matches expected.
        book_lover = BookLover("Mary Brown", "mary@gmail.com", "historical fiction")
        book_lover.add_book("Pride and Prejudice", 5)
        book_lover.add_book("To Kill a Mockingbird", 4)
        book_lover.add_book("1984", 3)
        self.assertEqual(book_lover.num_books_read(), 3)

    def test_6_fav_books(self):
        # Add some books with ratings to the list, making sure some of them have rating > 3.
        # Your test should check that the returned books have rating > 3.
        book_lover = BookLover("David Lee", "david@gmail.com", "adventure")
        book_lover.add_book("The Hobbit", 5)
        book_lover.add_book("Jurassic Park", 4)
        book_lover.add_book("Moby-Dick", 3)
        book_lover.add_book("The Da Vinci Code", 4)
        book_lover.add_book("The Catcher in the Rye", 5)
        fav_books = book_lover.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))

if __name__ == '__main__':
    unittest.main(verbosity=3)
