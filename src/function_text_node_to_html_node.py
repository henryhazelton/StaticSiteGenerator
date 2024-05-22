from textnode import TextNode
from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_bold:
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == text_type_text:
        return LeafNode(value=text_node.text)
    elif text_node.text_type == text_type_italic:
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == text_type_code:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == text_type_link:
        return LeafNode(tag="a", value=text_node.text, props=text_node.props)
    elif text_node.text_type == text_type_image:
        return LeafNode(tag="img", value="", props=text_node.props)
    else:
        raise ValueError("Invalid text type entered.")

