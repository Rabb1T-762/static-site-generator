class MockLeafNode:
    def __init__(self, tag, value, props=None):
        self.tag = tag
        self.value = value
        self.props = props

    def props_to_html(self):
        if not self.props:
            return ""
        return ' ' + ' '.join(f'{key}="{value}"' for key, value in self.props.items())

    def to_html(self):
        if self.value is None:
            raise ValueError(f"Error. No Value Provided in MockLeafNode: {self}")
        if self.tag == "":
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

