
def getFileLines(filename):
    with open(filename, "rb") as file:
        return file.read().splitlines()

def flip(data) -> list:
    return list(zip(*data))

def joinList(iterable):
    return ("".join([str(iter) for iter in iterable]))
