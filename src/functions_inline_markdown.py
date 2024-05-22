import re  

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_images(nodes)
    nodes = split_nodes_links(nodes)
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    # A loop may be needed here to iterate over the old_nodes list to then check each type
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        # This above checks if the type (aka what will be the tag) of the TextNode is in the form of plain text, if it is not, no further processing needed and thus added to list of new nodes
        else:
            # Now we need to implement a check to see if there are no missing delimiter tags, which can be done as follows:
            delimiter_count = old_node.text.count(delimiter)
            if delimiter_count % 2 != 0:
                raise Exception("There seems to be no closing delimiter, please check your inputs.")

            # I am going to create a tempoary list and use the extend function to add the new nodes to the new_nodes list, I am using this with the aim to increase performance!
            temporary_nodes = []
            parts_for_conversion = old_node.text.split(delimiter)
            # This loop below allows us to loop through the list 'parts_for_converison' and also keep track of the index whilst accessing the content inside the list
            for i, part in enumerate(parts_for_conversion):
            # 'i' holds the index which i need to check if the part is either in or outside the delimiter
            # part holds the value where I will need to change or keep as text_type_text
                if part:
                    text_type_to_use = text_type_text if i % 2 == 0 else text_type
                    text_node = TextNode(part, text_type_to_use)
                    temporary_nodes.append(text_node)
                    # This above, firstly checks whether the part is an empty string or not, 'if part:' is basically saying, if the part is not an empty string, continue
                    # Then, we create a variable which has a checking option inside it (ternary operator)
                    # If the index is an even number, the text node created for the part is of the type text
                    # If the index is odd, indicating text inside a delimiter that needs to be altered, we assign it the text type given in the function parameter
                    # Then we append the new text node created to the new nodes list at the top of the function.
            new_nodes.extend(temporary_nodes)
    return new_nodes


# Now we need to create a function that splits text into TextNodes when there is a link or image, very similar to splitting based on delimiters!

def split_nodes_images(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        temporary_nodes = []
        for image_tuple in extract_markdown_images(text):
            image_text, image_url = image_tuple
            delimiter = f"![{image_text}]({image_url})"
            text_before_image, text_after_image = text.split(delimiter, 1)
            # The text before the image will be a text node.
            # The text after could still contain images so could potentially need to be split more, hence changing text to text_after_image
            if text_before_image != "":
                text_node_text = TextNode(text_before_image, text_type_text)
                temporary_nodes.append(text_node_text)
            text_node_image = TextNode(image_text, text_type_image, url=image_url)
            temporary_nodes.append(text_node_image)
            text = text_after_image
            ######################################################################
        if text != "":
            text_node_text = TextNode(text, text_type_text)
            temporary_nodes.append(text_node_text)
        new_nodes.extend(temporary_nodes)
    return new_nodes


def split_nodes_links(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        temporary_nodes = []
        for link_tuple in extract_markdown_links(text):
            alt_text, url = link_tuple
            delimiter = f"[{alt_text}]({url})"
            text_before_link, text_after_link = text.split(delimiter, 1)
            # The text before the image will be a text node.
            # The text after could still contain images so could potentially need to be split more, hence changing text to text_after_image
            if text_before_link != "":
                text_node_text = TextNode(text_before_link, text_type_text)
                temporary_nodes.append(text_node_text)
            
            text_node_link = TextNode(alt_text, text_type_link, url=url)
            temporary_nodes.append(text_node_link)
            text = text_after_link
            ######################################################################
        if text != "":
            text_node_text = TextNode(text, text_type_text)
            temporary_nodes.append(text_node_text)
        new_nodes.extend(temporary_nodes)
    return new_nodes

# This function below will extract images from markdown text, which will be needed to convert into HTML
def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    images = re.findall(pattern, text)
    return images


# Same story for the links in markdown. The regex funciton is great for extracting patterns, ableit confusing af.
def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    links = re.findall(pattern, text)
    return links