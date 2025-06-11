import os
import shutil

from pathlib import Path
from functions_block_markdown import markdown_to_html_node

def copy_directory(src, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
        print(f"Created clean directory: {dest}")
    
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
            print(f"Copied file: {src_path} to {dest_path}")
        elif os.path.isdir(src_path):
            copy_directory(src_path, dest_path)  # Recursive call

def clear_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
        print(f"Removed directory and its contents: {directory}")
    clean_directory = os.makedirs(directory)
    print(f"Created clean directory: {directory}")
    return clean_directory
# This function removes the destination directory and then recreates it as a clean one each time

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return str(line.strip("# ").strip)
    raise Exception("Markdown file must contain a h1 heading")
    
# def generate_page(from_path, template_path, dest_path):
#   print(f"Generating page from {from_path} to {dest_path} using {template_path}")
#
#    # Read markdown file
#
#    with open(from_path, "r") as markdown_file:
#        markdown_file_contents = markdown_file.read()
#    
#    # Read template file
#
#    with open(template_path, "r") as template_file:
#        template_file_contents = template_file.read()
#    
#    # Convert markdown to HTML  
#
#    markdown_to_HTML = markdown_to_html_node(markdown_file_contents)
#
    # Extract title from markdown
#
#    title = extract_title(markdown_file_contents)

    # Replace placeholders in template

#    HTML_file = template_file_contents.replace("{{ Title }}", title)
#    HTML_file = HTML_file.replace("{{ Content }}", markdown_to_HTML.to_html())

    # Write HTML to destination path

#    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
#    with open(dest_path, "w") as output_file:
#        output_file.write(HTML_file)

#    print(f"Page successfully generated at {dest_path}")
def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)

########################################################################################################################
# def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
#    list_of_files_and_dirs = os.listdir(dir_path_content)
#    for item in list_of_files_and_dirs:
#        # Make source path which will be the path item is on
#        source_path = os.path.join(dir_path_content, item)
#        # Make destination path which is where we want item to go
#        destination_path = os.path.join(dest_dir_path, item.replace('.md', '.html'))#
#
#        # Check if item at end of source path is a file
#        if os.path.isfile(source_path) and item.endswith('.md'):
#            os.makedirs(dest_dir_path, exist_ok=True)
#            generate_page(source_path, template_path, destination_path)
#        elif os.path.isdir(source_path):
#            new_dest_dir_path = os.path.join(dest_dir_path, item)
#            generate_pages_recursively(source_path, template_path, new_dest_dir_path)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)