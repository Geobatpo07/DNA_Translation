import unittest
from src.translator.py import translate

class TestTranslator(unittest.TestCase):

    def test_translate_valid_sequence(self):
        seq = "ATGTGTATA"
        result = translate(seq)
        self.assertEqual(result, "MCI")

    def test_translate_invalid_codon(self):
        seq = "ATGTGTATX"
        result = translate(seq)
        self.assertEqual(result, "MC?")

    def test_translate_sequence_with_padding(self):
        seq = "ATGTGT"
        result = translate(seq)
        self.assertEqual(result, "MC")

if __name__ == '__main__':
    unittest.main()
