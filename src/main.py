print("Hello World!")

from textnode import TextNode
from functions_website_generation import clear_directory, copy_directory

def main():
    node = TextNode('Some Text', 'Bold', 'https://example.com')

    print(node)

    node2 = TextNode('Testing Testing Testing', 'Bold', 'https://example.com')

    print(node2)

    copy_directory('static', 'public')


if __name__ == "__main__":
    main()