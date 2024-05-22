import unittest

from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
from function_text_node_to_html_node import text_node_to_html_node

class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_bold_conversion(self):
        text_node = TextNode(text_type="bold", text="Test Bold")
        result = text_node_to_html_node(text_node)
        self.assertIsInstance(result, LeafNode)
        self.assertEqual(result.tag, "b")
        self.assertEqual(result.value, "Test Bold")

    def test_text_conversion(self):
        text_node = TextNode(text_type="text", text="Test Text")
        result = text_node_to_html_node(text_node)
        self.assertIsInstance(result, LeafNode)
        self.assertEqual(result.tag, None)
        self.assertEqual(result.value, "Test Text")

    def test_italic_conversion(self):
        text_node = TextNode(text_type="italic", text="Test Italic")
        result = text_node_to_html_node(text_node)
        self.assertIsInstance(result, LeafNode)
        self.assertEqual(result.tag, "i")
        self.assertEqual(result.value, "Test Italic")
    
    def test_code_conversion(self):
        text_node = TextNode(text_type="code", text="Test Code")
        result = text_node_to_html_node(text_node)
        self.assertIsInstance(result, LeafNode)
        self.assertEqual(result.tag, "code")
        self.assertEqual(result.value, "Test Code")

    def test_link_conversion(self):
        href_value = "https://example.com"
        link_text = "Example Link"
        text_node = TextNode(text_type="link", text=link_text, props={"href": href_value})
        result = text_node_to_html_node(text_node)
        self.assertIsInstance(result, LeafNode)
        self.assertEqual(result.tag, "a")
        self.assertEqual(result.value, link_text)
        self.assertTrue("href" in result.props)
        self.assertEqual(result.props["href"], href_value)
    
    def test_image_conversion(self):
        src_value = "https://example.com"
        alt_value = "[Insert Text to Describe the Image]"
        text_node = TextNode(text_type="image", text="", props={"src": src_value, "alt": alt_value})
        result = text_node_to_html_node(text_node)
        self.assertIsInstance(result, LeafNode)
        self.assertEqual(result.tag, "img")
        self.assertEqual(result.value, "")
        self.assertEqual(result.props["src"], src_value)
        self.assertEqual(result.props["alt"], alt_value)

    def test_invalid_conversion(self):
        text_node = TextNode(text_type="underlined", text="Test Raise Exception")
        with self.assertRaises(ValueError):
            result = text_node_to_html_node(text_node)


if __name__ == "__main__":
    unittest.main()
