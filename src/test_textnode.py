import unittest

from textnode import TextNode


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

        # Act
        for node, invalid_node, expected in test_cases:
            with self.subTest(node=node, invalid_node=invalid_node):
                print(f"""Running sub-test:
                        When passed an invalid node throws an error:
                        expecting {node} == {invalid_node}
                        to raise {expected}"""),
        # Assert
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
            (TextNode("This is a text node", "234", "http://link.dev"),
             TextNode("This is a text node", "234", "http://link.dev"),
             True),
            (TextNode("1234 567", ""),
             TextNode("1234 567", "",),
             True),
            (TextNode("%$[]", "%$", "http://link.dev"),
             TextNode("%$[]", "%$", "http://link.dev"),
             True),
        ]

        # Act
        for node, node2, expected in test_cases:
            with self.subTest(node=node, node2=node2):
                print(f"""Running sub-test:
                      expecting {node} == {node2}
                      to be {expected}"""),

        # Assert
                self.assertEqual(node == node2, expected)

    def test_eq_when_passed_two_different_nodes_returns_false(self):
        # Arrange
        test_cases = [
            (TextNode("%$[]", "%$", "http://link.dev"),
             TextNode("%$[]", "%$"),
             False),
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
             TextNode("This is a text node", "bald"),
             False),
            (TextNode("This is a text node", "234", "http://link.dev"),
             TextNode("This is a text node", "234", "http://link.de"),
             False),
            (TextNode("This is a text node", "234", "http://link.dev"),
             TextNode("This is a text node", "234", "http:/ link.dev"),
             False),
            ]

        # Act
        for node, node2, expected in test_cases:
            with self.subTest(node=node, node2=node2):
                print(f"""Running sub-test:
                      expecting {node} == {node2}
                      to be {expected}"""),

        # Assert
                self.assertEqual(node == node2, expected)


class TestTextNodeRepr(unittest.TestCase):
    def test_repr_prints_the_correct_representation(self):
        # Arrange
        test_cases = [
            (TextNode("This is a text node", "bold"),
             "TextNode(This is a text node, bold, None)"),
            (TextNode("This is a text node", "italic"),
             "TextNode(This is a text node, italic, None)"),
            (TextNode("This is a text node", "234", "http://link.dev"),
             "TextNode(This is a text node, 234, http://link.dev)"),
            (TextNode("1234 567", ""),
             "TextNode(1234 567, , None)"),
            (TextNode("%$[]", "%$", "http://link.dev"),
             "TextNode(%$[], %$, http://link.dev)"),
            ]

        # Act
        for node, expected in test_cases:
            with self.subTest(node=node):
                print(f"""Running sub-test:
                      expecting {node}.__repr__()
                      to be {expected}"""),

        # Assert
                self.assertEqual(node.__repr__(), expected)


if __name__ == '__main__':
    unittest.main()
