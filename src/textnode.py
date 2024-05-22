text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    def __init__(self, text, text_type, url=None, props=None):
        if text is None:
            raise ValueError("Text cannot be none, please enter text.")
            
        self.text = text
        self.text_type = text_type
        self.url = url
        self.props = props
    
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return "TextNode({}, {}, {})".format(self.text, self.text_type, self.url)
    

