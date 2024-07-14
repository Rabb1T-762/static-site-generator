from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)
        self.children = children

    def to_html(self):
        if self.tag == "":
            raise ValueError(
                    f"Error. No Tag Provided in ParentNode: {self}")
        if not self.children:
            raise ValueError(
                    f"Error. No Children Provided in ParentNode: {self}")
        return f"<{self.tag}{self.props_to_html()}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"

