import os
import unittest
from my_find.my_find import my_find


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_name = "test"
        result = my_find(dir_path, file_name)
        self.assertEqual(result, None)


if __name__ == "__main__":

    unittest.main()
