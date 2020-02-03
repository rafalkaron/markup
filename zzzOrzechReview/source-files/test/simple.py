import io
import unittest
import filecmp
import os.path


class TestSimpleConversions(unittest.TestCase):

    def test_split(self):
        #tu trzeba będzie tak przerobić, żeby czytało z /resources/readme_markup.md i zapisywało gdzieś, następnie porównać te pliki
        tst_path = '/Users/orzech/dupa/readme_markup.dita'
        self.assertTrue(os.path.isfile(tst_path))
        ref_path = '/Users/orzech/dupa/readme_markup_expected.dita'
        # self.assertTrue(filecmp.cmp(tst_path, ref_path), "Files are not identical!")
        self.assertListEqual(
            list(io.open(tst_path)),
            list(io.open(ref_path)))


if __name__ == '__main__':
    unittest.main()
