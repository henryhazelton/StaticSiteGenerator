print("Hello World!")

from textnode import TextNode

def main():
    node = TextNode('Some Text', 'Bold', 'https://example.com')

    print(node)

    node2 = TextNode('Testing Testing Testing', 'Bold', 'https://example.com')

    print(node2)

if __name__ == "__main__":
    main()