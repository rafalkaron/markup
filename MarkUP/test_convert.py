import unittest
import mock
import os
import shutil
from MarkUP import Source


class TestConvert(unittest.TestCase):

    def setUp(self):
        self.md_a_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/md/a.md"
        self.md_to_dita_out = "/Users/rafalkaron/GitHub/MarkUP/tests/data/md/a.dita"
        self.md_to_html_out = "/Users/rafalkaron/GitHub/MarkUP/tests/data/md/a.html"

        self.html_a_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/html/a.html"
        self.html_to_dita_out = "/Users/rafalkaron/GitHub/MarkUP/tests/data/html/a.dita"
        self.html_to_md_out = "/Users/rafalkaron/GitHub/MarkUP/tests/data/html/a.md"

        self.dita_a_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/dita/a.dita"
        self.dita_to_html_out = "/Users/rafalkaron/GitHub/MarkUP/tests/data/dita/a.dita"
        self.dita_to_md_out = "/Users/rafalkaron/GitHub/MarkUP/tests/data/dita/a.md"

        self.md_b_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/md/b.md"
        self.html_b_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/html/b.html"
        self.dita_b_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/dita/b.dita"

        self.md_c_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/md/C.md"
        self.html_c_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/html/C.html"
        self.dita_c_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/dita/C.dita"

        self.md_dir = "/Users/rafalkaron/GitHub/MarkUP/tests/data/md"
        self.html_dir = "/Users/rafalkaron/GitHub/MarkUP/tests/data/html"
        self.dita_dir = "/Users/rafalkaron/GitHub/MarkUP/tests/data/dita"

        self.output_dir = "/Users/rafalkaron/GitHub/MarkUP/tests/data/out"
        # shutil.rmtree(self.output_dir)
        try:
            os.remove(self.md_to_dita_out)
        except:
            pass
        # os.remove(self.md_to_html_out)

    def test_md_to_dita_file(self):
        source = Source(self.md_a_filepath, "md_dita")
        with mock.patch('builtins.input', return_value="y"):
            output_filepath = source.convert()[0]
        self.assertTrue(os.path.isfile(output_filepath))

    def test_md_to_html_file(self):
        source = Source(self.md_a_filepath, "md_html")
        with mock.patch('builtins.input', return_value="y"):
            output_filepath = source.convert()[0]
        self.assertTrue(os.path.isfile(output_filepath))

    def test_html_to_dita_file(self):
        try:
            os.remove(self.md_a_filepath.replace(".html", ".dita"))
        except:
            pass

        source = Source(self.html_b_filepath, "html_dita")
        with mock.patch('builtins.input', return_value="y"):
            output_filepath = source.convert()[0]
        self.assertTrue(os.path.isfile(output_filepath))

    def test_html_to_md_file(self):
        try:
            os.remove(self.md_a_filepath.replace(".html", ".md"))
        except:
            pass

        source = Source(self.html_b_filepath, "html_md")
        with mock.patch('builtins.input', return_value="y"):
            output_filepath = source.convert()[0]
        self.assertTrue(os.path.isfile(output_filepath))
