import unittest
import mock
import os
from MarkUP import Source


class TestConvert(unittest.TestCase):

    def setUp(self):
        self.md_a_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/a.md"
        self.html_a_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/a.html"
        self.dita_a_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/a.dita"
        self.md_b_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/a.md"
        self.html_b_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/a.html"
        self.dita_b_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/a.dita"

    def test_md_to_dita_file(self):
        try:
            os.remove(self.dita_a_filepath)
        except:
            pass

        source = Source(self.md_a_filepath, "md_dita")
        with mock.patch('builtins.input', return_value="y"):
            output_file = source.convert()[0]
        self.assertEqual(output_file, self.dita_a_filepath)
        self.assertTrue(os.path.isfile(output_file))

    def test_md_to_html(self):
        try:
            os.remove(self.html_a_filepath)
        except:
            pass

        source = Source(self.md_a_filepath, "md_html")
        with mock.patch('builtins.input', return_value="y"):
            output_file = source.convert()[0]
        self.assertEqual(output_file, self.html_a_filepath)
        self.assertTrue(os.path.isfile(output_file))
