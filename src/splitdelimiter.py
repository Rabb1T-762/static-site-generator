from textnode import TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_nodes = []

    if not isinstance(old_nodes, list):
        raise ValueError("old_nodes must be a list")

    if delimiter == "":
        return old_nodes

    for node in old_nodes:
        if not isinstance(node, TextNode):
            split_nodes.append(node)
        else:
            text_node_array = split_text_to_nodes_array(
                node.text, delimiter, text_type
            )
            split_nodes.extend(text_node_array)

    return split_nodes


def create_text_node(text, text_type):
    return TextNode(text, text_type)


# Recursively split the text into nodes array
def split_text_to_nodes_array(text, delimiter, text_type, nodes=None):
    if nodes is None:
        nodes = []

    delimiter_open = text.find(delimiter)
    # There are no delimiters in the text
    if delimiter_open == -1:
        nodes.append(create_text_node(text, "text"))
        return nodes

    # Find the closing delimiter
    delimiter_close = text.find(delimiter, delimiter_open + len(delimiter))
    if delimiter_close == -1:
        # Invalid syntax if the delimiter is not closed
        raise ValueError("Delimiter not closed")

    if delimiter_open > 0:
        nodes.append(create_text_node(text[:delimiter_open], "text"))

    nodes.append(
        create_text_node(
            text[delimiter_open + len(delimiter):delimiter_close],
            text_type
        )
    )

    if delimiter_close + len(delimiter) < len(text):
        split_text_to_nodes_array(
            text[delimiter_close + len(delimiter):],
            delimiter,
            text_type,
            nodes
        )

    return nodes
