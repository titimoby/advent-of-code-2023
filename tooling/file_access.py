def get_content(filename: str) -> list[str]:
    with open(filename, "r") as file:
        content = file.readlines()
    return content
