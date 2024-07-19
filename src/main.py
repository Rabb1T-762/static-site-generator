from textnode import TextNode
from splitdelimiter import split_nodes_delimiter, split_text_to_nodes_array


def main():
    new_node = TextNode("Hi there!", "bold", "http://link.dev")
    print(new_node)

    print("*" * 25)
    print("TESTING split_nodes_delimiter")

    node = TextNode("This is text with a `code block` word", "text")
    new_nodes = split_nodes_delimiter([node], "`", "code")

    # print(split_text_to_nodes_array(new_node2.text, "*", "italic"))
    print(new_nodes)


main()
