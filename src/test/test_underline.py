from unittest import TestCase

from underlines import underline
from underlines import book


class TestUnderlineFinder(TestCase):

    def test_find_underlines(self):
        underlines = underline.find_underlines("9788960516175")
        assert type(underlines) is list
        assert type(underlines[0]) is str

    def test_save(self):
        ## Given
        underline.init_table()
        book.init_table()
        found = book.find("9791160560367")
        book.save(found)
        ## When
        key = underline.save("9791160560367", "underline")
        ## Then
        saved = underline.get("9791160560367")
        assert saved['underline'] == "underline"