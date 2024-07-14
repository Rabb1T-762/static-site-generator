import unittest

from parentnode import ParentNode
from mocks.mock_leafnode import MockLeafNode


class TestParentNodeToHTML(unittest.TestCase):
    def test_when_called_with_no_tag_throws_value_error(self):
        # Arrange
        parent = ParentNode("", None, None)

        # Act
        # Assert
        with self.assertRaisesRegex(
                ValueError,
                "Error. No Tag Provided in ParentNode:"):
            parent.to_html()

    def test_when_called_with_no_children_throws_value_error(self):
        # Arrange
        error = {
                "type": ValueError,
                "value": "Error. No Children Provided in ParentNode:"
        }

        test_cases = [
                ("div", None, None),
                ("div", [], None),
                ("div", "", None),
        ]

        # Act
        for tag, children, props in test_cases:
            parent = ParentNode(tag, children, props)

        # Assert
            with self.assertRaisesRegex(error["type"], error["value"]):
                parent.to_html()

    def test_when_called_with_correct_inputs_returns_string_of_correct_html(self):
        # Arrange
        test_cases = [
            (
                "div",
                [MockLeafNode("p", "Hello")],
                None,
                "<div><p>Hello</p></div>"
            ),
            (
                "div",
                [MockLeafNode("p", "Hello"),
                 MockLeafNode("p", "World")],
                None,
                "<div><p>Hello</p><p>World</p></div>"
            ),
            (
                "div",
                [MockLeafNode("p", "Hello"), MockLeafNode("p", "World")],
                {"class": "container"},
                '<div class="container"><p>Hello</p><p>World</p></div>'
            ),
            (
                "test",
                [ParentNode("div",
                            [MockLeafNode("p", "Hello"),
                             MockLeafNode("b", "World"),
                             MockLeafNode("p", "!")],
                            {"class": "sub-container"})],
                {"class": "container"},
                '<test class="container"><div class="sub-container"><p>Hello</p><b>World</b><p>!</p></div></test>'
            ),
        ]

        # Act
        for tag, children, props, expected in test_cases:
            parent = ParentNode(tag, children, props)
            result = parent.to_html()

            # Assert
            self.assertEqual(result, expected)
