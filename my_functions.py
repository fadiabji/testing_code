#Here put some functions for future use
def return_file_content(filename):
    """This function to print the file content"""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        return(f"The file '{filename}' is not exsit in the directory")
    else:
        return(contents)

