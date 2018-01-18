from unittest import TestCase

from underlines import book_finder

class TestBookFinder(TestCase):

    def test_find_book(self):
         book = book_finder.find_book(9791160560367)
         assert book['title'] == "말이 칼이 될 때 - 혐오표현은 무엇이고 왜 문제인가?"

    def test_find_blogbest_isbn13(self):
        isbn13s = book_finder.find_blogbest_isbn13()
        print(isbn13s)
        assert len(isbn13s) == 10
        for isbn13 in isbn13s:
            assert len(isbn13) == 13
