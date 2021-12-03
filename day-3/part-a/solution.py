def solve(file_name: str) -> int:
    with open(file_name, "r") as file_handler:
        lines: list[str] = file_handler.readlines()
        digit_amount: int = len(lines[0].replace("\n", ""))

        gamma_rate = ""
        epsilon_rate = ""

        for index in range(digit_amount):
            digits = [
                line[index] for line in lines
            ]
            amt_1 = digits.count("1")
            amt_0 = digits.count("0")

            gamma_rate += "1" if amt_1 > amt_0 else "0"
            epsilon_rate += "0" if amt_1 > amt_0 else "1"

        return int(gamma_rate, 2) * int(epsilon_rate, 2)

print("Sample input solution: ", solve("sample_input"))
print("Real input solution: ", solve("input"))
