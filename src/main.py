print("Hello World!")

import sys
from functions_website_generation import clear_directory, copy_directory, generate_pages_recursive


src_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"


def main():
    clear_directory(dir_path_public)

    copy_directory(src_path_static, dir_path_public)

    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)

if __name__ == "__main__":
    main()