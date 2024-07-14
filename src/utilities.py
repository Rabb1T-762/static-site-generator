from leafnode import LeafNode
from textnode import TextNode


def text_node_to_html_node(text_node):
    types = ["text"]
    if text_node.text_type not in types:
        raise ValueError(f"Unknown TextNode Type: {text_node}")

    return LeafNode("", text_node.text)
