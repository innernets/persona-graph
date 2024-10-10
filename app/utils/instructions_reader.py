def read_instructions():
    with open("INSTRUCTIONS.md", "r") as file:
        return file.read()

INSTRUCTIONS = read_instructions()
