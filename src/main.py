print("Hello World!")

from textnode import TextNode
from functions_website_generation import clear_directory, copy_directory, generate_page, extract_title, generate_pages_recursive

src_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    clear_directory(dir_path_public)

    copy_directory(src_path_static, dir_path_public)

    generate_pages_recursive(dir_path_content, template_path, dir_path_public)

main()

if __name__ == "__main__":
    main()