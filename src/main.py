print("Hello World!")

from textnode import TextNode
from functions_website_generation import clear_directory, copy_directory, generate_page, extract_title

src_path_static = "./static"
dest_path_static = "./public"

def main():
    node = TextNode('Some Text', 'Bold', 'https://example.com')

    print(node)

    node2 = TextNode('Testing Testing Testing', 'Bold', 'https://example.com')

    print(node2)

    copy_directory(src_path_static, dest_path_static)

    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()