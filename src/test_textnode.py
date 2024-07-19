import unittest

from textnode import TextNode, VALID_TEXT_NODE_TYPES


class TestTextNode(unittest.TestCase):
    def test_init_with_invalid_text_type_raises_exception(self):
        # Arrange
        invalid_text_types = ["invalid", "not_a_type", 123, None]

        # Act & Assert
        for invalid_type in invalid_text_types:
            with self.subTest(invalid_type=invalid_type):
                print(f"Running sub-test: expecting TextNode with text_type {invalid_type} to raise ValueError")
                with self.assertRaises(ValueError):
                    TextNode("This is a text node", invalid_type)

    def test_init_with_valid_text_type_does_not_raise_exception(self):
        # Arrange
        valid_text_types = list(VALID_TEXT_NODE_TYPES.keys())

        # Act & Assert
        for valid_type in valid_text_types:
            with self.subTest(valid_type=valid_type):
                print(f"Running sub-test: expecting TextNode with text_type {valid_type} to not raise an exception")
                try:
                    TextNode("This is a text node", valid_type)
                except ValueError:
                    self.fail(f"TextNode raised ValueError unexpectedly for valid text_type {valid_type}")


class TestTextNodeEq(unittest.TestCase):
    def test_eq_when_called_with_an_invalid_input_throws_an_error(self):
        # Arrange
        test_cases = [
                (TextNode("This is a text node", "bold"),
                 "This is a text node",
                 AttributeError),
                (TextNode("This is a text node", "bold"),
                 23,
                 AttributeError),
                ]

        # Act & Assert
        for node, invalid_node, expected in test_cases:
            with self.subTest(node=node, invalid_node=invalid_node):
                print(f"Running sub-test: expecting {node} == {invalid_node} to raise {expected}")
                with self.assertRaises(expected):
                    _ = node == invalid_node

    def test_eq_when_passed_two_equal_nodes_returns_true(self):
        # Arrange
        test_cases = [
            (TextNode("This is a text node", "bold"),
             TextNode("This is a text node", "bold"),
             True),
            (TextNode("This is a text node", "italic"),
             TextNode("This is a text node", "italic"),
             True),
            (TextNode("This is a text node", "text", "http://link.dev"),
             TextNode("This is a text node", "text", "http://link.dev"),
             True),
        ]

        # Act & Assert
        for node, node2, expected in test_cases:
            with self.subTest(node=node, node2=node2):
                print(f"Running sub-test: expecting {node} == {node2} to be {expected}")
                self.assertEqual(node == node2, expected)

    def test_eq_when_passed_two_different_nodes_returns_false(self):
        # Arrange
        test_cases = [
            (TextNode("This is a text node", "bold"),
             TextNode("This is a text node", "italic"),
             False),
            (TextNode("2342 928", "bold"),
             TextNode("This is a text node", "italic"),
             False),
            (TextNode("2342 928", "bold"),
             TextNode("2342 938", "bold"),
             False),
            (TextNode("This is a text node", "bold"),
             TextNode("This is a text node", "code"),
             False),
            (TextNode("This is a text node", "text", "http://link.dev"),
             TextNode("This is a text node", "text", "http://link.de"),
             False),
            (TextNode("This is a text node", "text", "http://link.dev"),
             TextNode("This is a text node", "text", "http:/ link.dev"),
             False),
        ]

        # Act & Assert
        for node, node2, expected in test_cases:
            with self.subTest(node=node, node2=node2):
                print(f"Running sub-test: expecting {node} == {node2} to be {expected}")
                self.assertEqual(node == node2, expected)


class TestTextNodeRepr(unittest.TestCase):
    def test_repr_prints_the_correct_representation(self):
        # Arrange
        test_cases = [
            (TextNode("This is a text node", "bold"),
             "TextNode(This is a text node, bold, None)"),
            (TextNode("This is a text node", "italic"),
             "TextNode(This is a text node, italic, None)"),
            (TextNode("This is a text node", "text", "http://link.dev"),
             "TextNode(This is a text node, text, http://link.dev)"),
        ]

        # Act & Assert
        for node, expected in test_cases:
            with self.subTest(node=node):
                print(f"Running sub-test: expecting {node}.__repr__() to be {expected}")
                self.assertEqual(node.__repr__(), expected)
