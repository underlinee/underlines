from unittest import TestCase

from underlines.domain import underline, book


class TestUnderline(TestCase):

    def test_find_underlines(self):
        underlines = underline.find_underlines("8960516171")
        assert type(underlines) is list
        assert type(underlines[0]) is str

    def test_save(self):
        ## Given
        underline.init_table()
        book.init_table()
        found = book.find_by_isbn13("9791160560367")
        book.save(found)
        ## When
        key = underline.save("9791160560367", "underline")
        ## Then
        saved = underline.get_by_isbn13("9791160560367")
        assert saved['underline'] == "underline"