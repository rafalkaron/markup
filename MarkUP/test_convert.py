import unittest
import mock
import os
from MarkUP import Source


class TestConvert(unittest.TestCase):

    def test_md_to_dita_file(self):
        source = Source(
            "/Users/rafalkaron/GitHub/MarkUP/tests/data/README.md", "md_dita", "")
        with mock.patch('builtins.input', return_value="y"):
            output_file = source.convert()
        self.assertTrue(os.path.isfile(output_file[0]))
