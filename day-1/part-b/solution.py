with open("input", "r") as file_handler:
    window_length = 3

    lines = file_handler.readlines()
    measurements = [
        sum(
            tuple(
                int(lines[i+j]) for j in range(window_length)
            )
        )
        for i in range(len(lines) - window_length + 1)
    ]
    print([measurements[i] > measurements[i-1] for i in range(1, len(measurements))].count(True))
