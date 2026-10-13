def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def write_file(filename, data):
    with open(filename, "w") as file:
        file.writelines(data)


def append_file(filename, data):
    with open(filename, "a") as file:
        file.write(data)