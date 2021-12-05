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

        winners, called = [], []
        while len(winners) != len(boards):
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
            winners.extend([
                idx for idx in range(len(boards_that_win))
                if idx not in winners and boards_that_win[idx]
            ])

        winner_board_uncalled_numbers = []
        last_winner = winners[-1]
        for row in range(5):
            for column in range(5):
                if boards[last_winner][row][column] not in called:
                    winner_board_uncalled_numbers.append(boards[last_winner][row][column])

        return called[-1] * sum(winner_board_uncalled_numbers)



print("Sample input solution: ", solve("sample_input"))
print("Real input solution: ", solve("input"))
