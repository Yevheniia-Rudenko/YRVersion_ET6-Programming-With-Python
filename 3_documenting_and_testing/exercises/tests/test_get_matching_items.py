import unittest

from ..get_matching_items import get_matching_items

class TestGetMatchingItems(unittest.TestCase):
    """Test the get_matching_items function"""

    def test_strings_with_letter(self):
        """It should return strings with the letter."""
        self.assertEqual(get_matching_items(["apple", "banana", "cherry", "grape"], "a"), ["apple", "banana", "grape"])

    def test_lists_with_value(self):
        """It should return lists containing the value."""
        self.assertEqual(get_matching_items([[1, 2], [3, 4], [5, 6, 2]], 2), [[1, 2], [5, 6, 2]])

    def test_no_matching_elements(self):
        """It should return an empty list if no matches are found."""
        self.assertEqual(get_matching_items(["hello", "world", "python"], "z"), [])

    def test_empty_input_list(self):
        """It should return an empty list for an empty input."""
        self.assertEqual(get_matching_items([], "a"), [])

    def test_mismatched_element_types(self):
        """It should raise TypeError if types do not match."""
        with self.assertRaises(TypeError):
            get_matching_items([1, 2, 3], "a")
        
    def test_non_iterable_argument(self):
        """It should raise TypeError for None input."""
        with self.assertRaises(TypeError):
            get_matching_items(None, "a")
