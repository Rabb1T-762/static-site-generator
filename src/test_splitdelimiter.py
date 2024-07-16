import unittest

import splitdelimiter


class Test_SplitDelimiter(unittest.TestCase):
    def test_when_passed_empty_array_returns_empty_array(self):
        # Arrange
        old_nodes = []
        expected = []
        text_type = "text"

        # Act
        actual = splitdelimiter.split_nodes_delimiter(
                old_nodes, " ", text_type
                )

        # Assert
        self.assertEqual(expected, actual)
