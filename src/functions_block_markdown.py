block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

from htmlnode import ParentNode
from functions_inline_markdown import text_to_textnodes
from function_text_node_to_html_node import text_node_to_html_node


def markdown_to_blocks(markdown):
    block_strings = []
    potential_blocks = markdown.split("\n\n")
    for block in potential_blocks:
        stripped_block = block.strip()
        if stripped_block == "":
            continue
        block_strings.append(stripped_block)
    return block_strings


def block_to_block_type(markdown_block):
    line_in_block = markdown_block.split("\n")

    if (
        markdown_block.startswith("# ")
        or markdown_block.startswith("## ")
        or markdown_block.startswith("### ")
        or markdown_block.startswith("#### ")
        or markdown_block.startswith("##### ")
        or markdown_block.startswith("###### ")
    ):
        return block_type_heading

    if (
        len(markdown_block) > 1
        and line_in_block[0].startswith("```")
        and line_in_block[-1].startswith("```")
    ):
        return block_type_code

    elif markdown_block.startswith(">"):
        is_quote_block = True
        for line in line_in_block:
            if line.startswith(">"):
                continue
            else:
                is_quote_block = False
        if is_quote_block:
            return block_type_quote

    elif markdown_block.startswith("*") or markdown_block.startswith("-"):
        is_unordered_list = True
        for line in line_in_block:
            if line.startswith("*") or line.startswith("-"):
                continue
            else:
                is_unordered_list = False
        if is_unordered_list:
            return block_type_unordered_list

    elif markdown_block[0].isdigit() and markdown_block[1] == ".":
        is_ordered_list = True
        list_number = 0
        for line in line_in_block:
            list_number += 1
            if line.startswith(f"{list_number}. "):
                is_ordered_list = True
            else:
                is_ordered_list = False
        if is_ordered_list:
            return block_type_ordered_list

    else:
        return block_type_paragraph


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


# This ^ funciton above is used to create the children property that will be passed into ParentNode.
# How and why it is done this way is a mystery to me and something I will slowly get through, however I will not be defeated!


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    main_html_node = ParentNode(tag="div", children=children)
    return main_html_node


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_block_to_html_node(block)
    if block_type == block_type_code:
        return code_block_to_html_node(block)
    if block_type == block_type_heading:
        return heading_block_to_html_node(block)
    if block_type == block_type_quote:
        return quote_block_to_html_node(block)
    if block_type == block_type_ordered_list:
        return ordered_list_to_html_node(block)
    if block_type == block_type_unordered_list:
        return unordered_list_block_to_html_node(block)
    else:
        raise ValueError("Invalid block type given.")


def paragraph_block_to_html_node(block):
    single_line_block = " ".join(block.split("\n"))
    children = text_to_children(single_line_block)
    paragraph_node = ParentNode(tag="p", children=children)
    return paragraph_node


def heading_block_to_html_node(block):
    block_parts = block.split(" ", 1)
    heading_level = len(block_parts[0])  # This counts the number of "#" in the heading
    heading_text = (
        block_parts[1] if len(block_parts) > 1 else ""
    )  # This gives us the heading text that can be passed into htmlnode
    tag_name = "h" + str(heading_level)
    children = text_to_children(heading_text)
    heading_node = ParentNode(tag=tag_name, children=children)
    return heading_node


def code_block_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    code_content = block[3:-3]
    children = text_to_children(code_content)
    code_node = ParentNode(tag="code", children=children)
    pre_node = ParentNode(tag="pre", children=[code_node])
    return pre_node


def quote_block_to_html_node(block):
    lines_in_block = block.split("\n")
    clean_block = []
    for line in lines_in_block:
        if line.startswith(">"):
            clean_line = line.lstrip("> ").lstrip()
            clean_block.append(clean_line)
    clean_block_str = " ".join(clean_block)
    children = text_to_children(clean_block_str)
    quote_block = ParentNode(tag="blockquote", children=children)
    return quote_block


def unordered_list_block_to_html_node(block):
    children_items = []
    individual_children = block.split("\n")
    for child in individual_children:
        clean_child = child[2:]
        child_nodes = text_to_children(clean_child)
        li_node = ParentNode(tag="li", children=child_nodes)
        children_items.append(li_node)
    ul_node = ParentNode(tag="ul", children=children_items)
    return ul_node


def ordered_list_to_html_node(block):
    children_items = []
    individual_children = block.split("\n")
    for child in individual_children:
        clean_child = child[3:]
        child_nodes = text_to_children(clean_child)
        li_node = ParentNode(tag="li", children=child_nodes)
        children_items.append(li_node)
    ol_node = ParentNode(tag="ol", children=children_items)
    return ol_node
