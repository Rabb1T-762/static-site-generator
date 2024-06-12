import unittest

from htmlnode import HTMLNode


class TestHTMLNodePropsToHTML(unittest.TestCase):
    def test_props_to_html_returns_correct_html_props(self):
        # Arrange
        test_cases = [
            ({"href": "https://www.google.com", "target": "_blank"},
             ' href="https://www.google.com" target="_blank"'),
            ({"class": "btn btn-primary", "data-toggle": "modal"},
             ' class="btn btn-primary" data-toggle="modal"'),
            ({"id": "modal", "data-target": "#modal"},
             ' id="modal" data-target="#modal"'),
        ]
        for input_props, expected in test_cases:
            # Act
            node = HTMLNode(props=input_props)
            print(node.props)
            result = node.props_to_html()
            print(result)

            # Assert
            self.assertEqual(result, expected)


class TestHTMLNodeRepr(unittest.TestCase):
    def test_repr_returns_correct_string(self):
        # Arrange
        test_cases = [
            (HTMLNode("a", "Click me", props={"href": "https://www.google.com"}),
             "HTMLNode(a, Click me, None, {'href': 'https://www.google.com'})"),
            (HTMLNode("button", "Submit", props={"class": "btn btn-primary"}),
             "HTMLNode(button, Submit, None, {'class': 'btn btn-primary'})"),
            (HTMLNode("div", "Hello", children=[HTMLNode("p", "World")]),
             "HTMLNode(div, Hello, [HTMLNode(p, World, None, None)], None)"),
        ]
        for node, expected in test_cases:
            # Act
            result = repr(node)

            # Assert
            self.assertEqual(result, expected)
