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
        self.md_c_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/C.md"
        self.html_c_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/C.html"
        self.dita_c_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/C.dita"
        self.output_dir = "out"

    def test_md_to_dita_file(self):
        try:
            os.remove(self.dita_a_filepath)
        except:
            pass

        source = Source(self.md_a_filepath, "md_dita")
        with mock.patch('builtins.input', return_value="y"):
            output_filepath = source.convert()[0]
        self.assertEqual(output_filepath, self.dita_a_filepath)
        self.assertTrue(os.path.isfile(output_filepath))

    def test_md_to_html_file(self):
        try:
            os.remove(self.html_a_filepath)
        except:
            pass

        source = Source(self.md_a_filepath, "md_html")
        with mock.patch('builtins.input', return_value="y"):
            output_filepath = source.convert()[0]
        self.assertEqual(output_filepath, self.html_a_filepath)
        self.assertTrue(os.path.isfile(output_filepath))

    def test_html_to_dita_file(self):
        try:
            os.remove(self.dita_b_filepath)
        except:
            pass

        source = Source(self.html_b_filepath, "html_dita")
        with mock.patch('builtins.input', return_value="y"):
            output_filepath = source.convert()[0]
        self.assertEqual(output_filepath, self.dita_b_filepath)
        self.assertTrue(os.path.isfile(output_filepath))

    def test_html_to_md_file(self):
        try:
            os.remove(self.md_b_filepath)
        except:
            pass

        source = Source(self.html_b_filepath, "html_md")
        with mock.patch('builtins.input', return_value="y"):
            output_filepath = source.convert()[0]
        self.assertEqual(output_filepath, self.md_b_filepath)
        self.assertTrue(os.path.isfile(output_filepath))
