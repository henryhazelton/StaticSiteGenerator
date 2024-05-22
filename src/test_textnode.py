import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", "bold", None)
        self.assertIsNone(node.url)
    
    def test_test_type(self):
        node = TextNode("This is a test node", "italic", "https://example.com")
        node2 = TextNode("This is a test node", "bold", "https://example.com")
        self.assertNotEqual(node, node2)
    
    def test_empty_text_raises_error(self):
        with self.assertRaises(ValueError):
            node = TextNode(None, "bold", "https://example.com")

    def test_text_length(self):
        lengthy_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        node = TextNode(lengthy_text, "bold", "https://example.com")
        self.assertEqual(node.text, lengthy_text)


if __name__ == "__main__":
    unittest.main()
