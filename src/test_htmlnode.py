import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        result = node.__repr__()
        self.assertEqual(
            result,
            "HTMLNode(tag=None, value=None, children=None, props={'href': 'https://www.google.com', 'target': '_blank'})",
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode(
            "a",
            "This is a paragraph of text.",
            props={"href": "https://www.google.com"},
        )
        result = node.to_html()
        self.assertEqual(
            result, '<a href="https://www.google.com">This is a paragraph of text.</a>'
        )

    def test_no_tag(self):
        node = LeafNode(
            None,
            "This is a paragraph of text.",
            props={"href": "https://www.google.com"},
        )
        result = node.to_html()
        self.assertEqual(result, "This is a paragraph of text.")

    def test_no_value(self):
        node = LeafNode("a", None, props={"href": "https://www.google.com"})
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertFalse(
            "All leafnodes must contain a value." in str(context.exception)
        )

        # We use the assertRaises method as a context manager using the with statement. This way, the test anticipates the ValueError when executing node.to_html().
        # Inside the with block, we call the method that is expected to raise the error.
        # After the block, you can optionally check the error message using context.exception to ensure it contains the expected text, although this step is often not necessary unless you need to validate the specific error message.

    def test_no_props(self):
        node = LeafNode("a", "This is a test", None)
        result = node.to_html()
        self.assertEqual(result, "<a>This is a test</a>")


class TestParentNode(unittest.TestCase):
    def test_single_level_nesting(self):
        node = ParentNode(
            "div", [LeafNode("p", "Paragraph 1"), LeafNode("p", "Paragraph 2")]
        )
        result = node.to_html()
        self.assertEqual(result, "<div><p>Paragraph 1</p><p>Paragraph 2</p></div>")

    def test_double_level_nesting(self):
        node = ParentNode(
            "div",
            [
                LeafNode("h1", "Main Title"),
                ParentNode(
                    "section",
                    [
                        LeafNode("p", "Paragraph in section"),
                        LeafNode(
                            "a", "Link text", props={"href": "https://example.com"}
                        ),
                    ],
                ),
            ],
        )
        result = node.to_html()
        self.assertEqual(
            result,
            '<div><h1>Main Title</h1><section><p>Paragraph in section</p><a href="https://example.com">Link text</a></section></div>',
        )

    def empty_children(self):
        with self.assertRaises(ValueError) as context:
            node = ParentNode("div", [])
        self.assertTrue(
            "ParentNode must contain at least one child argument"
            in str(context.exception)
        )

    def test_parent_node_with_mixed_content(self):
        node = ParentNode(
            "ul",
            [
                LeafNode(None, "This is text directly in a ul."),
                ParentNode("li", [LeafNode(None, "Item 1")]),
                ParentNode("li", [LeafNode("p", "Paragraph in item 2")]),
            ],
        )

        # The expected HTML output
        expected_html = "<ul>This is text directly in a ul.<li>Item 1</li><li><p>Paragraph in item 2</p></li></ul>"

        # Generate HTML from the node structure
        actual_html = node.to_html()

        # Assert that the actual HTML matches the expected HTML
        self.assertEqual(actual_html, expected_html)

    def test_instructors_example(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        expected_html = (
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

        actual_html = node.to_html()

        self.assertEqual(actual_html, expected_html)

    def test_deep_nesting_with_multiple_child_nodes(self):
        # Setup your deeply nested nodes structure
        node = ParentNode(
            "div",
            [
                LeafNode("h2", "Section Title"),
                ParentNode(
                    "ul",
                    [
                        ParentNode(
                            "li",
                            [
                                LeafNode("p", "Item 1 text."),
                                LeafNode(
                                    "a",
                                    "Click here",
                                    {"href": "https://example.com/item1"},
                                ),
                            ],
                        ),
                        ParentNode(
                            "li",
                            [
                                LeafNode("p", "Item 2 text."),
                                ParentNode(
                                    "div", [LeafNode("span", "More details here.")]
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )

        # Define the expected HTML output
        expected_html = '<div><h2>Section Title</h2><ul><li><p>Item 1 text.</p><a href="https://example.com/item1">Click here</a></li><li><p>Item 2 text.</p><div><span>More details here.</span></div></li></ul></div>'

        # Generate the HTML output from your node structure
        actual_html = node.to_html()

        # Assert that the actual HTML matches the expected output
        self.assertEqual(actual_html, expected_html)


if __name__ == "__main__":
    unittest.main()
