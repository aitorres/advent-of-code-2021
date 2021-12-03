def solve(file_name: str) -> int:
    with open(file_name, "r") as file_handler:
        lines: list[str] = file_handler.readlines()
        digit_amount: int = len(lines[0].replace("\n", ""))

        o2_rate = ""
        co2_rate = ""

        o2_lines, co2_lines = lines.copy(), lines.copy()
        for index in range(digit_amount):
            if o2_rate != "" and co2_rate != "":
                break

            if o2_rate == "":
                o2_digits = [
                    line[index] for line in o2_lines
                ]
                amt_1 = o2_digits.count("1")
                amt_0 = o2_digits.count("0")
                o2_lines = [
                    line for line in o2_lines
                    if line[index] == (
                        "1" if amt_1 >= amt_0 else "0"
                    )
                ]

                if len(o2_lines) == 1:
                    o2_rate = o2_lines[0]

            if co2_rate == "":
                co2_digits = [
                    line[index] for line in co2_lines
                ]
                amt_1 = co2_digits.count("1")
                amt_0 = co2_digits.count("0")
                co2_lines = [
                    line for line in co2_lines
                    if line[index] == (
                        "0" if amt_1 >= amt_0 else "1"
                    )
                ]

                if len(co2_lines) == 1:
                    co2_rate = co2_lines[0]

        return int(o2_rate, 2) * int(co2_rate, 2)

print("Sample input solution: ", solve("sample_input"))
print("Real input solution: ", solve("input"))
