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

        x = sum(
            [moves for command, moves in commands if command == "forward"]
        )
        y = sum(
            [
                (
                    -moves
                    if command == "up"
                    else moves
                )
                for command, moves in commands if command != "forward"
            ]
        )
        return x * y

print("Sample input solution: ", solve("sample_input"))
print("Real input solution: ", solve("input"))
