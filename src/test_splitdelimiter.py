import unittest
from textnode import TextNode

import splitdelimiter


class Test_SplitDelimiter(unittest.TestCase):
    def test_when_passed_invalid_input_raises_exception(self):
        # Arrange
        test_cases = [
             ("invalid_type", "*", "text"),
             (123, "*", "text"),
             (None, "*", "text"),
             ]

        # Act
        # Assert
        for old_nodes, delimiter, text_type in test_cases:
            with self.assertRaises(ValueError):
                splitdelimiter.split_nodes_delimiter(
                        old_nodes, delimiter, text_type
                        )

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

    def test_when_passed_non_text_node_returns_the_node(self):
        # Arrange
        test_cases = [
                    (["a", "b", "c"], "*", "text", ["a", "b", "c"]),
                    (["a"], "*", "text", ["a"]),
                    (["a"], "*", "text", ["a"]),
                    ]

        for old_nodes, delimiter, text_type, expected in test_cases:
            # Act
            actual = splitdelimiter.split_nodes_delimiter(
                    old_nodes, delimiter, text_type
                    )

            # Assert
            self.assertEqual(expected, actual)

    def test_when_passed_empty_delimiter_returns_input_array(self):
        # Arrange
        test_cases = [
                    ([TextNode("This is a test", "text"),
                        TextNode("This is another test node", "text")],
                     "",
                     [TextNode("This is a test", "text"),
                      TextNode("This is another test node", "text"),]),
                    (["a", "b", "c"], "", ["a", "b", "c"]),
                    (["a"], "", ["a"]),
                    ([], "", []),
                    ]
        for old_nodes, delimiter, expected in test_cases:
            # Act
            actual = splitdelimiter.split_nodes_delimiter(
                    old_nodes, delimiter, "text"
                    )

            # Assert
            self.assertEqual(expected, actual)

    def test_when_passed_text_node_with_italic_delimiter_returns_split_nodes(self):
        # Arrange
        old_nodes = [
                TextNode("This is a test", "text"),
                TextNode("This is an *italic* test node", "text"),
                TextNode("This is *another italic test*", "text"),
                ]
        delimiter = "*"
        text_type = "italic"
        expected = [
                TextNode("This is a test", "text"),
                TextNode("This is an ", "text"),
                TextNode("italic", "italic"),
                TextNode(" test node", "text"),
                TextNode("This is ", "text"),
                TextNode("another italic test", "italic"),
                ]

        # Act
        actual = splitdelimiter.split_nodes_delimiter(
                old_nodes, delimiter, text_type
                )

        # Assert
        self.assertEqual(expected, actual)

    def test_when_passed_text_node_with_bold_delimiter_returns_split_nodes(self):
        # Arrange
        old_nodes = [
                TextNode("This is a test", "text"),
                TextNode("This is an **bold** test node", "text"),
                TextNode("This is **another bold test**", "text"),
                ]
        delimiter = "**"
        text_type = "bold"
        expected = [
                TextNode("This is a test", "text"),
                TextNode("This is an ", "text"),
                TextNode("bold", "bold"),
                TextNode(" test node", "text"),
                TextNode("This is ", "text"),
                TextNode("another bold test", "bold"),
                ]

        # Act
        actual = splitdelimiter.split_nodes_delimiter(
                old_nodes, delimiter, text_type
                )

        # Assert
        self.assertEqual(expected, actual)

    def test_when_passed_text_node_with_bold_delimiter_returns_split_nodes(self):
        # Arrange
        old_nodes = [
                TextNode("This is a test", "text"),
                TextNode("This is an **bold** test node", "text"),
                TextNode("This is **another bold test**", "text"),
                TextNode("This is a **double bold** test with **another bold delimiter**", "text"),
                ]
        delimiter = "**"
        text_type = "bold"
        expected = [
                TextNode("This is a test", "text"),
                TextNode("This is an ", "text"),
                TextNode("bold", "bold"),
                TextNode(" test node", "text"),
                TextNode("This is ", "text"),
                TextNode("another bold test", "bold"),
                TextNode("This is a ", "text"),
                TextNode("double bold", "bold"),
                TextNode(" test with ", "text"),
                TextNode("another bold delimiter", "bold"),
                ]

        # Act
        actual = splitdelimiter.split_nodes_delimiter(
                old_nodes, delimiter, text_type
                )

        # Assert
        self.assertEqual(expected, actual)

        def test_when_passed_text_node_with_code_delimiter_returns_split_nodes(self):
            # Arrange
            node = TextNode("This is text with a `code block` word", "code")

            # Act
            new_nodes = splitdelimiter.split_nodes_delimiter([node], "`", "code")

            # Assert
            self.assertListEqual(
                [
                    TextNode("This is text with a ", "code"),
                    TextNode("code block", "code"),
                    TextNode(" word", "code"),
                ],
                new_nodes,
            )


class Test_SplitDelimiter_SplitTextToNodesArray(unittest.TestCase):
    def test_when_passed_text_and_delimiter_returns_nodes_array(self):
        # Arrange
        test_cases = [
                ("This is a test",
                 "*",
                 "italic",
                 [
                    TextNode("This is a test", "text"),
                    ]),
                ("This is *a test*",
                 "*",
                 "italic",
                 [
                    TextNode("This is ", "text"),
                    TextNode("a test", "italic"),
                    ]),
                ("This is *a test* and *another test*",
                 "*",
                 "italic",
                 [
                    TextNode("This is ", "text"),
                    TextNode("a test", "italic"),
                    TextNode(" and ", "text"),
                    TextNode("another test", "italic"),
                    ]),
                ]

        for text, delimiter, text_type, expected in test_cases:
            # Act
            actual = splitdelimiter.split_text_to_nodes_array(text, delimiter, text_type)

            # Assert
            self.assertEqual(expected, actual)
