"""
Create your own extractors, and package them below!
"""
def get_file_contents(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def execute_extractor(file_path):
    mdata = {
        'contents': get_file_contents(file_path),
    }

    return mdata


if __name__ == "__main__":
    print(execute_extractor("requirements.txt"))