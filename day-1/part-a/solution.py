with open("input", "r") as file_handler:
    lines = file_handler.readlines()
    print([int(lines[i]) > int(lines[i-1]) for i in range(1, len(lines))].count(True))
