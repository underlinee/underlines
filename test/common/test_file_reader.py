from unittest import TestCase

from underlines.common import file_reader


class TestFileReader(TestCase):
    def test_analize_entities(self):
        txts = file_reader.read_txts()
        assert type(txts) is list
        assert type(txts[0]) is str