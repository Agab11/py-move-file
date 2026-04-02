import os


def move_file(command: str) -> None:
    if not command:
        return

    parts = command.split()
    if len(parts) != 3:
        return

    action, source_path, destination = parts
    if action != "mv":
        return

    if destination.endswith("/"):
        final_path = destination + source_path
    else:
        final_path = destination

    path_parts = final_path.split("/")
    directories = path_parts[:-1]

    current_path = ""
    for directory in directories:
        if not directory:
            continue

        if current_path == "":
            current_path = directory
        else:
            current_path += "/" + directory

        if not os.path.exists(current_path):
            os.mkdir(current_path)

    with open(source_path, "r") as source_file:
        content = source_file.read()

    with open(final_path, "w") as destination_file:
        destination_file.write(content)

    os.remove(source_path)
