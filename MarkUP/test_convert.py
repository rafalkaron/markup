import unittest
import os
from MarkUP import Source


class TestConvert(unittest.TestCase):

    def test_md_dita_file(self):
        source = Source(
            "/Users/rafalkaron/GitHub/MarkUP/tests/data/README.md", "md_dita")
        Source.output_file = source.convert()

        self.assertTrue(os.path.isfile(Source.output_file))
