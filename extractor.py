#TODO: 2) add a folder with 3 or 4 test files

"""
Create your own extractor subcomponents, following the model below.
"""
def get_file_contents(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_file_len(file_contents):
    """Returns the number of lines in a file.
    Parameter:
    file_path (str): Path of file to determine number of lines.
    Return:
    length (int): number of lines in a file.
    """
    length = 1
    for i in file_contents:
        if i == '\n':
            length += 1
    return length

def execute_extractor(file_path):
    """ The general model of extraction is for the method `execute_extractor` 
    to call extractor subcomponents. These results are typically store in a 
    dictionary and returned upon completion.
    """
    
    # Files should be opened as few times as possible to avoid expensive IO
    # calls (P3).
    file_contents = get_file_contents(file_path)

    mdata = {
        'length': get_file_len(file_contents)
    }

    return mdata


if __name__ == "__main__":
    print(execute_extractor("test/hello_world.py"))
    print(execute_extractor("test/lorem_ipsum.txt"))
    print(execute_extractor("test/on_time.txt"))
    
