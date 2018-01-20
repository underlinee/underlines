from unittest import TestCase

from underlines import book

class TestBookFinder(TestCase):

    def test_find(self):
         found = book.find("9791160560367")
         assert found['title'] == "말이 칼이 될 때 - 혐오표현은 무엇이고 왜 문제인가?"

    def test_find_blogbest_isbn13(self):
        isbn13s = book.find_blogbest_isbn13()
        assert len(isbn13s) == 10
        for isbn13 in isbn13s:
            assert len(isbn13) == 13

    def test_save(self):
        ## Given
        book.init_db()
        found = book.find("9791160560367")
        ## When
        book.save(found)
        ## Then
        saved = book.get("9791160560367")
        assert saved['title'] == "말이 칼이 될 때 - 혐오표현은 무엇이고 왜 문제인가?"