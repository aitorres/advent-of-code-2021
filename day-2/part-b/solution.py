def solve(file_name: str) -> int:
    with open(file_name, "r") as file_handler:
        lines = file_handler.readlines()
        clean_lines = [
            line.replace("\n", "").split()
            for line in lines
        ]

        commands = [
            (command[0], int(command[1]))
            for command in clean_lines
        ]

        aim = 0
        depth = 0
        horizontal_position = 0

        for command, moves in commands:
            if command == "forward":
                horizontal_position += moves
                depth += aim * moves
            else:
                aim += (
                    -moves
                    if command == "up"
                    else moves
                )

        return depth * horizontal_position

print("Sample input solution: ", solve("sample_input"))
print("Real input solution: ", solve("input"))
