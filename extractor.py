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
    to call extractor subcomponents and store the results in a dictionary.
    """
    
    file_contents = get_file_contents(file_path)

    mdata = {
        'contents': file_contents,
        'length': get_file_len(file_contents)
    }

    return mdata


if __name__ == "__main__":
    print(execute_extractor("requirements.txt"))
