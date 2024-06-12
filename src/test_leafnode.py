import unittest

from leafnode import LeafNode


class TestLeafNodeToHTML(unittest.TestCase):
    def test_when_called_with_no_value_throws_a_value_error(self):
        # Arrange
        leaf = LeafNode("p", None, None)

        # Act
        # Assert
        with self.assertRaisesRegex(ValueError, "Error. No Value Provided in LeafNode:") as context:
            leaf.to_html()

    def test_when_called_with_no_tag_returns_raw_text(self):
        # Arrange
        test_cases = [
            ("", "This is a paragraph of text.", "",
             "This is a paragraph of text."),
            ("", "Click me!", {"href": "https://www.google.com"},
             "Click me!"),
        ]

        # Act
        for tag, value, props, expected in test_cases:
            leaf = LeafNode(tag, value, props)
            result = leaf.to_html()

        # Assert
            self.assertEqual(result, expected)

    def test_when_passed_valid_input_returns_html_element(self):
        # Arrange
        test_cases = [
            ("p", "This is a paragraph of text.", "",
             "<p>This is a paragraph of text.</p>"),
            ("a", "Click me!", {"href": "https://www.google.com"},
             '<a href="https://www.google.com">Click me!</a>'),
        ]

        # Act
        for tag, value, props, expected in test_cases:
            leaf = LeafNode(tag, value, props)
            result = leaf.to_html()

        # Assert
            self.assertEqual(result, expected)
