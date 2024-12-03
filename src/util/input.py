def read_lines(filepath: str):
    with open(filepath, "r") as file:
        return file.read().splitlines()

def read(filepath: str):
    with open(filepath, "r") as file:
        return file.read()