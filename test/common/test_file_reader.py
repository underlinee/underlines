from unittest import TestCase

from underlines.common import file_reader


class TestFileReader(TestCase):
    def test_read_txts(self):
        txts = file_reader.read_txts()
        assert type(txts) is list
        assert type(txts[0]) is str

    def test_read_lines(self):
        lines = file_reader.read_lines("isbns.txt")
        assert type(lines) is list
        assert len(lines) is 100