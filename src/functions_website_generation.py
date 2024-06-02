import os
import shutil

from functions_block_markdown import markdown_to_html_node

def copy_directory(src, dest):
    clear_directory(dest)
    # I need this function to copy all the data and files in one directory and then paste them into another directory, we can do this!

    # This if statement above check whether the destination directory exsists first before anything else is done
    # If the directory does not exsist, then we make the destination directory, now we shall go on to code the copying of source directory content
    for item in os.listdir(src):
        # The first thing i need to do it to construct full source and destination file paths
        # This is needed so the function knows exactly where to put the files, in other words, there is no ambiguity
        # This can be done as such:
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        # item is a file or directory
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
            # This above checks whether the item is a file, if so, it copies the src_path to the dest_path
            # The parameter is src_path as that is the path we want to copy
            print(f"Copied file: {src_path} to {dest_path}")  # This logs for visability into what is happening
        elif os.path.isdir(src_path):
            copy_directory(src_path, dest_path)

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
    
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read markdown file

    with open(from_path, "r") as markdown_file:
        markdown_file_contents = markdown_file.read()
    
    # Read template file

    with open(template_path, "r") as template_file:
        template_file_contents = template_file.read()
    
    # Convert markdown to HTML  

    markdown_to_HTML = markdown_to_html_node(markdown_file_contents)

    # Extract title from markdown

    title = extract_title(markdown_file_contents)

    # Replace placeholders in template

    HTML_file = template_file_contents.replace("{{ Title }}", title)
    HTML_file = HTML_file.replace("{{ Content }}", markdown_to_HTML.to_html())

    # Write HTML to destination path

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as output_file:
        output_file.write(HTML_file)

    print(f"Page successfully generated at {dest_path}")