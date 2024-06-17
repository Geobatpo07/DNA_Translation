import unittest
from src.utils import read_file, write_file
import os

class TestUtils(unittest.TestCase):

    def test_read_file(self):
        content = read_file('data/dna.txt')
        self.assertTrue(isinstance(content, str))

    def test_write_file(self):
        test_content = "ATGC"
        write_file('data/test_output.txt', test_content)
        with open('data/test_output.txt', 'r') as f:
            content = f.read()
        self.assertEqual(content, test_content)
        os.remove('data/test_output.txt')

if __name__ == '__main__':
    unittest.main()
