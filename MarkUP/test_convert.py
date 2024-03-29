from MarkUP.files import files_list
import unittest
import mock
import os
import shutil
from MarkUP import Source


md_a_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/md/a.md"
md_a_dita_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/md/a.dita"
md_a_html_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/md/a.html"

html_a_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/html/a.html"
html_a_dita_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/html/a.dita"
html_a_md_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/html/a.md"

dita_a_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/dita/a.dita"
dita_a_html_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/dita/a.dita"
dita_a_md_filepath = "/Users/rafalkaron/GitHub/MarkUP/tests/data/dita/a.md"

md_dir = "/Users/rafalkaron/GitHub/MarkUP/tests/data/md"
html_dir = "/Users/rafalkaron/GitHub/MarkUP/tests/data/html"
dita_dir = "/Users/rafalkaron/GitHub/MarkUP/tests/data/dita"

output_dir = "/Users/rafalkaron/GitHub/MarkUP/tests/data/out"


class TestConvertFile(unittest.TestCase):

    def test_md_to_dita(self):
        try:
            os.remove(md_a_filepath.replace(".md", ".dita"))
        except:
            pass

        source = Source(md_a_filepath, "md_dita")
        with mock.patch('builtins.input', return_value="y"):
            output_filepath = source.convert()[0]
        self.assertTrue(os.path.isfile(output_filepath))
        self.assertEqual(output_filepath, md_a_dita_filepath)

    def test_md_to_html(self):
        try:
            os.remove(md_a_filepath.replace(".md", ".html"))
        except:
            pass

        source = Source(md_a_filepath, "md_html")
        with mock.patch('builtins.input', return_value="y"):
            output_filepath = source.convert()[0]
        self.assertTrue(os.path.isfile(output_filepath))
        self.assertEqual(output_filepath, md_a_html_filepath)

    def test_html_to_dita(self):
        try:
            os.remove(html_a_filepath.replace(".html", ".dita"))
        except:
            pass

        source = Source(html_a_filepath, "html_dita")
        with mock.patch('builtins.input', return_value="y"):
            output_filepath = source.convert()[0]
        self.assertTrue(os.path.isfile(output_filepath))
        self.assertEqual(output_filepath, html_a_dita_filepath)

    def test_html_to_md(self):
        try:
            os.remove(html_a_filepath.replace(".html", ".md"))
        except:
            pass

        source = Source(html_a_filepath, "html_md")
        with mock.patch('builtins.input', return_value="y"):
            output_filepath = source.convert()[0]
        self.assertTrue(os.path.isfile(output_filepath))
        self.assertEqual(output_filepath, html_a_md_filepath)


class TestConvertFileOutput(unittest.TestCase):

    def test_md_to_dita(self):
        try:
            shutil.rmtree(output_dir)
        except:
            pass

        source = Source(md_a_filepath, "md_dita", output_dir)
        with mock.patch('builtins.input', return_value="y"):
            output_filepath = source.convert()[0]
        self.assertTrue(os.path.isfile(output_filepath))

    def test_md_to_html(self):
        try:
            shutil.rmtree(output_dir)
        except:
            pass

        source = Source(md_a_filepath, "md_html", output_dir)
        with mock.patch('builtins.input', return_value="y"):
            output_filepath = source.convert()[0]
        self.assertTrue(os.path.isfile(output_filepath))

    def test_html_to_dita(self):
        try:
            shutil.rmtree(output_dir)
        except:
            pass

        source = Source(html_a_filepath, "html_dita", output_dir)
        with mock.patch('builtins.input', return_value="y"):
            output_filepath = source.convert()[0]
        self.assertTrue(os.path.isfile(output_filepath))

    def test_html_to_md(self):
        try:
            shutil.rmtree(output_dir)
        except:
            pass

        source = Source(html_a_filepath, "html_md", output_dir)
        with mock.patch('builtins.input', return_value="y"):
            output_filepath = source.convert()[0]
        self.assertTrue(os.path.isfile(output_filepath))


class TestConvertFolder(unittest.TestCase):
    def test_md_to_dita(self):

        output_files = files_list(md_dir, "dita")
        for i in output_files:
            os.remove(i)

        source = Source(md_dir, "md_dita")
        with mock.patch('builtins.input', return_value="a"):
            output_filepath = source.convert()

        for i in output_filepath:
            self.assertTrue(os.path.isfile(i))

    def test_md_to_html(self):

        output_files = files_list(md_dir, "html")
        for i in output_files:
            os.remove(i)

        source = Source(md_dir, "md_html")
        with mock.patch('builtins.input', return_value="a"):
            output_filepath = source.convert()

        for i in output_filepath:
            self.assertTrue(os.path.isfile(i))

    def test_html_to_dita(self):

        output_files = files_list(md_dir, "dita")
        for i in output_files:
            os.remove(i)

        source = Source(html_dir, "html_dita")
        with mock.patch('builtins.input', return_value="a"):
            output_filepath = source.convert()

        for i in output_filepath:
            self.assertTrue(os.path.isfile(i))

    def test_html_to_md(self):

        output_files = files_list(html_dir, "md")
        for i in output_files:
            os.remove(i)

        source = Source(html_dir, "html_md")
        with mock.patch('builtins.input', return_value="a"):
            output_filepath = source.convert()

        for i in output_filepath:
            self.assertTrue(os.path.isfile(i))


class TestConvertFolderOutput(unittest.TestCase):
    def test_md_to_dita(self):

        output_files = files_list(output_dir, "dita")
        for i in output_files:
            os.remove(i)

        source = Source(md_dir, "md_dita", output_dir)
        with mock.patch('builtins.input', return_value="a"):
            output_filepath = source.convert()

        for i in output_filepath:
            self.assertTrue(os.path.isfile(i))

    def test_md_to_html(self):

        output_files = files_list(output_dir, "html")
        for i in output_files:
            os.remove(i)

        source = Source(md_dir, "md_html", output_dir)
        with mock.patch('builtins.input', return_value="a"):
            output_filepath = source.convert()

        for i in output_filepath:
            self.assertTrue(os.path.isfile(i))

    def test_html_to_dita(self):

        output_files = files_list(output_dir, "dita")
        for i in output_files:
            os.remove(i)

        source = Source(html_dir, "html_dita", output_dir)
        with mock.patch('builtins.input', return_value="a"):
            output_filepath = source.convert()

        for i in output_filepath:
            self.assertTrue(os.path.isfile(i))

    def test_html_to_md(self):

        output_files = files_list(output_dir, "md")
        for i in output_files:
            os.remove(i)

        source = Source(html_dir, "html_md", output_dir)
        with mock.patch('builtins.input', return_value="a"):
            output_filepath = source.convert()

        for i in output_filepath:
            self.assertTrue(os.path.isfile(i))


class TestPromptOverwrite(unittest.TestCase):

    def test_abort(self):
        source = Source(html_dir, "html_dita", output_dir)

        with mock.patch('builtins.input', return_value=""):
            output_filepath = source.convert()
        self.assertEqual(output_filepath, [])

        with mock.patch('builtins.input', return_value="Aa"):
            output_filepath = source.convert()
        self.assertEqual(output_filepath, [])

        with mock.patch('builtins.input', return_value="na"):
            output_filepath = source.convert()
        self.assertEqual(output_filepath, [])

        with mock.patch('builtins.input', return_value="na"):
            output_filepath = source.convert()
        self.assertEqual(output_filepath, [])


class TestLogging(unittest.TestCase):

    def test_log_creation(self):

        source = Source(html_a_filepath, "html_dita")

        with mock.patch('builtins.input', return_value="y"):
            output_filepath = source.convert()[0]

        self.assertTrue(os.path.isfile("MarkUP.log"))
        os.remove("MarkUP.log")


if __name__ == '__main__':
    unittest.main()
