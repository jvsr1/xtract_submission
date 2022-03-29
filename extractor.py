"""
Create your own extractor subcomponents, following the model below. 
Subcomponents should be independent and not produce side-effects in
the input.
"""
def get_file_contents(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def execute_extractor(file_path):
    """ The general model of extraction is for the method `execute_extractor` 
    to call extractor subcomponents and store the results in a dictionary.
    """
    mdata = {
        'contents': get_file_contents(file_path),
    }

    return mdata


if __name__ == "__main__":
    print(execute_extractor("requirements.txt"))
