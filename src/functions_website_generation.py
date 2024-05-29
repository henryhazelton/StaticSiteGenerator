import os
import shutil

def copy_directory(src, dest):
    # I need this function to copy all the data and files in one directory and then paste them into another directory, we can do this!
    if not os.path.exists(dest):
        os.makedirs(dest)
    # This if statement above check whether the destination directory exsists first before anything else is done
    # If the directory does not exsist, then we make the destination directory, now we shall go on to code the copying of source directory content
    for item in os.listdir(src):
        # The first thing i need to do it to construct full source and destination file paths
        # This is needed so the function knows exactly where to put the files, in other words, there is no ambiguity
        # This can be done as such:
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        # item is a file or directory
        
