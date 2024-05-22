import unittest

from functions_block_markdown import markdown_to_blocks, block_to_block_type, markdown_to_html_node, block_to_html_node, paragraph_block_to_html_node, heading_block_to_html_node, code_block_to_html_node, quote_block_to_html_node, unordered_list_block_to_html_node, ordered_list_to_html_node
from functions_block_markdown import (
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
)
from textnode import TextNode
from test_htmlnode import HTMLNode, ParentNode

class TestFunctionsInBlockMarkdown(unittest.TestCase):
    def test_basic_functionality(self):
        # Test 1: Basic functionality with different types of blocks
        markdown = """# Heading

This is a paragraph with **bold** text.

- List item 1
- List item 2

Another paragraph."""

        expected_result = [
            "# Heading", 
            "This is a paragraph with **bold** text.", 
            "- List item 1\n- List item 2", 
            "Another paragraph.",
            ]
        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected_result)

    
    def test_multiple_newlines_and_whitespace(self):
        markdown = """

This is the first paragraph.


This is the second paragraph.    

"""
        expected_result = [
            "This is the first paragraph.",
            "This is the second paragraph.",
        ]

        result = markdown_to_blocks(markdown)
        self.assertEqual(result, expected_result)

    
    def test_empty_markdown(self):
        markdown = ""
        result = markdown_to_blocks(markdown)
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_markdown_with_only_whitespace(self):
        markdown = "    \n\n  "
        result = markdown_to_blocks(markdown)
        expected_result = []
        self.assertEqual(result, expected_result)

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )
    
    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )


    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

####################################################################################################################
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )
####################################################################################################################

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
#############################################################################################################################
    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )
#################################################################################################################
    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )
###################################################################################################################
    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )
##################################################################################################################
    def test_code_block(self):
        md = """
```print("Hello, world!")```

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><pre><code>print("Hello, world!")</code></pre></div>',
        )
######################################################################################################################
if __name__ == '__main__':
    unittest.main()