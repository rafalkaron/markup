import unittest
import mock
import os
import shutil
from MarkUP import Source


class TestConvert(unittest.TestCase):

    def setUp(self):
        self.md_a_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/md/a.md"
        self.md_a_dita_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/md/a.dita"
        self.md_a_html_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/md/a.html"

        self.html_a_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/html/a.html"
        self.html_a_dita_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/html/a.dita"
        self.html_a_md_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/html/a.md"

        self.dita_a_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/dita/a.dita"
        self.dita_a_html_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/dita/a.dita"
        self.dita_a_md_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/dita/a.md"

        self.md_dir = "/Users/rafalkaron/GitHub/MarkUP/tests/data/md"
        self.html_dir = "/Users/rafalkaron/GitHub/MarkUP/tests/data/html"
        self.dita_dir = "/Users/rafalkaron/GitHub/MarkUP/tests/data/dita"

        self.output_dir = "/Users/rafalkaron/GitHub/MarkUP/tests/data/out"

    def test_md_to_dita_file(self):
        try:
            os.remove(self.md_a_filepath.replace(".md", ".dita"))
        except:
            pass

        source = Source(self.md_a_filepath, "md_dita")
        with mock.patch('builtins.input', return_value="y"):
            output_filepath = source.convert()[0]
        self.assertTrue(os.path.isfile(output_filepath))

    def test_md_to_html_file(self):
        try:
            os.remove(self.md_a_filepath.replace(".md", ".html"))
        except:
            pass

        source = Source(self.md_a_filepath, "md_html")
        with mock.patch('builtins.input', return_value="y"):
            output_filepath = source.convert()[0]
        self.assertTrue(os.path.isfile(output_filepath))

    def test_html_to_dita_file(self):
        try:
            os.remove(self.html_a_filepath.replace(".html", ".dita"))
        except:
            pass

        source = Source(self.html_a_filepath, "html_dita")
        with mock.patch('builtins.input', return_value="y"):
            output_filepath = source.convert()[0]
        self.assertTrue(os.path.isfile(output_filepath))

    def test_html_to_md_file(self):
        try:
            os.remove(self.html_a_filepath.replace(".html", ".md"))
        except:
            pass

        source = Source(self.html_a_filepath, "html_md")
        with mock.patch('builtins.input', return_value="y"):
            output_filepath = source.convert()[0]
        self.assertTrue(os.path.isfile(output_filepath))
