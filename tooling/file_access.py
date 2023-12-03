def get_content(filename: str) -> list[str]:
    with open(filename, "r") as file:
        content = file.read().splitlines()
    return content
