import unittest

from utilities import text_node_to_html_node
from textnode import TextNode
from leafnode import LeafNode


class Test_TextNodeToHtmlNode(unittest.TestCase):
    def test_is_passed_unknown_type(self):
        # Arrange
        # Act
        text_node = TextNode("Unknown Text", "text")
        # This is to simulate a TextNode with invalid type passed in
        text_node.text_type = "unknown"

        # Assert
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

    def test_is_passed_text_type_and_returns_leafNode(self):
        # Arrange
        text_node = TextNode("Known Text Type", "text")
        expected = LeafNode

        # Act
        result = text_node_to_html_node(text_node)

        # Assert
        self.assertIsInstance(result, expected)

    def test_is_passed_text_type_and_returns_leafNode_with_no_tag_and_text(self):
        # Arrange
        text_node = TextNode("Expected Text", "text")
        expected = "Expected Text"
        # Act
        actual = text_node_to_html_node(text_node)

        # Assert
        self.assertEqual(actual.to_html(), expected)

    def test_is_passed_bold_type_and_returns_leafNode_with_b_tag_and_text(self):
        # Arrange
        text_node = TextNode("Expected Text", "bold")
        expected = "<b>Expected Text</b>"

        # Act
        actual = text_node_to_html_node(text_node)

        # Assert
        self.assertEqual(actual.to_html(), expected)

    def test_is_passed_italic_type_and_returns_leafNode_with_i_tag_and_text(self):
        # Arrange
        text_node = TextNode("Expected Text", "italic")
        expected = "<i>Expected Text</i>"

        # Act
        actual = text_node_to_html_node(text_node)

        # Assert
        self.assertEqual(actual.to_html(), expected)

    def test_is_passed_code_type_and_returns_leafNode_with_code_tag_and_text(self):
        # Arrange
        text_node = TextNode("print 'Hello World!'", "code")
        expected = "<code>print 'Hello World!'</code>"
        # Act
        actual = text_node_to_html_node(text_node)

        # Assert
        self.assertEqual(actual.to_html(), expected)

    def test_is_passed_link_type_and_returns_leafNode_with_a_tag_and_anchor_text_and_href_prop(self):
        # Arrange
        text_node = TextNode("Click Me!", "link", "https://www.google.com")
        expected = '<a href="https://www.google.com">Click Me!</a>'

        # Act
        actual = text_node_to_html_node(text_node)

        # Assert
        self.assertEqual(actual.to_html(), expected)

    def test_is_passed_image_type_and_returns_leaf_node_with_img_tag_and_src_alt_props(self):
        # Arrange
        text_node = TextNode("Image Alt Text", "image",
                             "http://example.com/image.png")
        expected_html = '<img src="http://example.com/image.png" alt="Image Alt Text"></img>'
    
        # Act
        actual = text_node_to_html_node(text_node)
    
        # Assert
        self.assertEqual(actual.to_html(), expected_html)
