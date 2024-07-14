import unittest

from utilities import text_node_to_html_node
from textnode import TextNode
from leafnode import LeafNode


class Test_TextNodeToHtmlNode(unittest.TestCase):
    def test_text_node_to_html_node_unknown_type(self):
        # Arrange
        # Act
        text_node = TextNode("Unknown Text", "unknown")

        # Assert
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

    def test_text_node_to_html_node_is_known_type_returns_leafNode(self):
        # Arrange
        text_node = TextNode("Known Text Type", "text")
        expected = LeafNode

        # Act
        result = text_node_to_html_node(text_node)

        # Assert
        self.assertIsInstance(result, expected)
