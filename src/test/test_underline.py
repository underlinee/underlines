from unittest import TestCase

from underlines import underline


class TestUnderlineFinder(TestCase):

    def test_find_underlines(self):
        underlines = underline.find_underlines(9788960516175)
        assert type(underlines) is list
        assert type(underlines[0]) is str