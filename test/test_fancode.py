import unittest
from fancode_checker import calculate_completion_percentage

class TestFanCodeTask(unittest.TestCase):
    def test_calculate_completion(self):
        todos = [{'completed': True}, {'completed': False}, {'completed': True}]
        self.assertEqual(calculate_completion_percentage(todos), 66.67)

if __name__ == '__main__':
    unittest.main()
