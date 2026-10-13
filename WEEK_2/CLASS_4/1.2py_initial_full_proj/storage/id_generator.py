from storage.file_handler import read_file


def generate_id(filename):
    data = read_file(filename)

    if not data:
        return 1

    ids = []

    for line in data:
        parts = line.strip().split("|")

        if parts and parts[0].isdigit():
            ids.append(int(parts[0]))

    return max(ids, default=0) + 1