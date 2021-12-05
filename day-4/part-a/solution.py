def solve(file_name: str) -> int:
    with open(file_name, "r") as file_handler:
        callable_numbers = [
            int(n) for n in file_handler.readline().split(",")
        ]
        file_handler.readline()

        boards, current_board = [], 0
        for line in file_handler.readlines():
            if len(boards) == current_board:
                boards.append([])

            if line == "\n":
                current_board += 1
            else:
                boards[current_board].append(
                    [
                        int(n) for n in line.split()
                    ]
                )

        winner, called = None, []
        while winner is None:
            called.append(callable_numbers.pop(0))

            boards_that_win = [
                any(
                    [
                        any(
                            all(
                                board[column][i] in called for i in range(5)
                            )
                            for column in range(5)
                        ),
                        any(
                            all(
                                board[i][row] in called for i in range(5)
                            )
                            for row in range(5)
                        ),
                    ]
                )
                for board in boards
            ]
            if True in boards_that_win:
                winner = boards_that_win.index(True)

        winner_board_uncalled_numbers = []
        for row in range(5):
            for column in range(5):
                if boards[winner][row][column] not in called:
                    winner_board_uncalled_numbers.append(boards[winner][row][column])

        return called[-1] * sum(winner_board_uncalled_numbers)



print("Sample input solution: ", solve("sample_input"))
print("Real input solution: ", solve("input"))
