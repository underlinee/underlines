from unittest import TestCase

from underlines import collector
from underlines.domain import underline, book, keyword


class TestCollector(TestCase):
    def test_collect(self):
        # Init
        keyword.init_table()
        underline.init_table()
        book.init_table()
        # When
        collector.collect("9788954637756")
        # Then
        book_dict = book.find_by_isbn13("9788954637756")
        underline_dict = underline.get_by_isbn13(book_dict['isbn13'])
        keywords_dict = keyword.get_by_isbn13("9788954637756")
        print(keywords_dict)
        assert len(keywords_dict) != 0