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
        if line.startswith("# ") not in lines:
            raise Exception("Markdown file must contain a h1 heading")
        if line.startswith("# "):
            return line
    
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    # Below will read the file from "from_path"
    markdown_file = open("content/index.md", "r")
    markdown_file_contents = markdown_file.read()
    markdown_file.close()
    # This section above should open the markdown file located at "from_path", store the contents of the file in the variable "markdown_file_contents"
    # and then close the file which we opened.
    # We will now repeat for the file located at "template_path"
    template_file = open("template.html", "r")
    template_file_contents = template_file.read()
    template_file.close()
    markdown_file_to_HTML = markdown_to_html_node(markdown_file_contents)
    title = str(extract_title(markdown_file_contents))
    HTML_file = template_file_contents.replace("{{ Title }}", title)
    HTML_file = HTML_file.replace("{{ Content }}", str(markdown_file_contents))
    copy_directory(from_path, dest_path)
    for item in os.listdir(from_path):
        src_path = os.path.join(from_path, item)
        dest_path = os.path.join(dest_path, item)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        


# Im not sure the above is right, markdown file to html is now HTML not markup, so I need to extract the title from markdown, not html