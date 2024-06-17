def read_file(file_path):
    """Read a file and return its content as a string, with special characters removed."""
    with open(file_path, "r") as f:
        seq = f.read()
    seq = seq.replace("\n", "")\
             .replace("\r", "")\
             .replace("\t", "")\
             .replace(" ", "")
    return seq

def write_file(file_path, content):
    """Write a string content to a file."""
    with open(file_path, "w") as f:
        f.write(content)
