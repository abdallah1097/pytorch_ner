import unittest

# TODO: fix it
import sys
sys.path.append('../pytorch_ner')
from prepare_data import prepare_conll_data_format, get_token2idx, get_label2idx
from utils import process_tokens, process_labels


token_seq, label_seq = prepare_conll_data_format('conll.txt')
token2idx = get_token2idx(token_seq)
label2idx = get_label2idx(label_seq)

tokens = ['Simple', 'is', 'better', 'than', 'complex', '.']
labels = ['O', 'O', 'O', 'O', 'O', 'B-Puctuation']


class TestUtils(unittest.TestCase):

    def test_process_tokens(self):
        self.assertEqual(
            process_tokens(tokens, token2idx),
            [1, 3, 4, 5, 1, 7],
        )

    def test_process_labels(self):
        self.assertEqual(
            process_labels(labels, label2idx),
            [0, 0, 0, 0, 0, 1],
        )
