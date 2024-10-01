import unittest
from quiz import check_answer
from unittest.mock import patch
from quiz_util import questions, answers

class TestCheckAnswer(unittest.TestCase):
    
    @patch('builtins.input', side_effect=[4, 22, 1.5, 1, 8])
    def test_check_answer_all_correct(self, mock_input):
        score = 0
        expected_score = 5
        result = check_answer(score)
        self.assertEqual(result, expected_score)

    @patch('builtins.input', side_effect=[4, 22, 1.5, 0, 0])
    def test_check_answer_partial_correct(self, mock_input):
        score = 0
        expected_score = 3
        result = check_answer(score)
        self.assertEqual(result, expected_score)

    @patch('builtins.input', side_effect=[0, 0, 0, 0, 0])
    def test_check_answer_all_wrong(self, mock_input):
        score = 0
        expected_score = 0
        result = check_answer(score)
        self.assertEqual(result, expected_score)
        
if __name__ == '__main__':
    unittest.main()