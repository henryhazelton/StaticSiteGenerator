class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        attributes_list = []
        for key, value in self.props.items():
            attributes_string = key + '="' + str(value) + '"'
            attributes_list.append(attributes_string)
        return " ".join(attributes_list)
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
            
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None: # prefer 'is' for comparison
            raise ValueError("All leafnodes must contain a value.")
        if self.tag is None:
            return str(self.value)
        # LeafNode("p", "This is a paragraph of text.")
        # LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        # goes to:
        # <p>This is a paragraph of text.</p>
        # <a href="https://www.google.com">Click me!</a>
    
        properties_string = self.props_to_html()

        # Add a space before properties_string only if it's not empty
        space_if_props = " " if properties_string else ""

        return f"<{self.tag}{space_if_props}{properties_string}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children):
        super().__init__(tag=tag)
        if not children:
            raise ValueError("ParentNode must contain at least one child argument")
        self.children = children
    # The above ensures that a ParentNode cannot be created unless there is a child or children (which is a list) included in the argument parameters

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag cannot be 'None', please enter a valid tag")
        
        html = f"<{self.tag}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"