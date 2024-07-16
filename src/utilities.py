from leafnode import LeafNode


def text_node_to_html_node(text_node):
    types = {"text": LeafNode("", text_node.text),
             "bold": LeafNode("b", text_node.text),
             "italic": LeafNode("i", text_node.text),
             "code": LeafNode("code", text_node.text),
             "link": LeafNode("a", text_node.text, {"href": text_node.url}),
             "image": LeafNode("img", "", {
                 "src": text_node.url, "alt": text_node.text
                 }),
             }
    if text_node.text_type not in types:
        raise ValueError(f"Unknown TextNode Type: {text_node}")

    return types[text_node.text_type]
