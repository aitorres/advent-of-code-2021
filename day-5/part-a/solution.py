from collections import defaultdict

from typing import Set, Tuple


def from_line_to_points(line: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    start, end = (
        point.strip().split(",")
        for point in line.split(" -> ")
    )
    start = (int(start[0]), int(start[1]))
    end = (int(end[0]), int(end[1]))
    return start, end


def from_points_to_set_of_marked_points(
    start: Tuple[int, int],
    end: Tuple[int, int],
) -> Set[Tuple[int, int]]:

    increment_y = start[0] == end[0]

    if not increment_y and start[1] != end[1]:
        return set()

    starting_point = start[0] if not increment_y else start[1]
    ending_point = end[0] if not increment_y else end[1]
    delta = ending_point - starting_point
    range_instance = (
        range(starting_point, ending_point + 1)
        if delta > 0
        else range(ending_point, starting_point + 1)
    )

    return {
        (start[0], j) if increment_y else (j, start[1])
        for j in range_instance
    }

assert from_line_to_points("777,778 -> 777,676") == ((777, 778), (777, 676))
assert from_points_to_set_of_marked_points(
    (1, 4),
    (1, 7),
) == {
    (1, 4),
    (1, 5),
    (1, 6),
    (1, 7),
}

assert from_points_to_set_of_marked_points(
    (5, 7),
    (1, 7),
) == {
    (1, 7),
    (2, 7),
    (3, 7),
    (4, 7),
    (5, 7),
}

def solve(file_name: str) -> int:
    with open(file_name, "r") as file_handler:
        vents = defaultdict(lambda: 0)

        for line in file_handler.readlines():
            start, end = from_line_to_points(line)

            increment_y = start[0] == end[0]
            starting_point = start[0] if not increment_y else start[1]
            ending_point = end[0] if not increment_y else end[1]
            delta = ending_point - starting_point

            points_to_increment = from_points_to_set_of_marked_points(start, end)
            for point_to_increment in points_to_increment:
                vents[point_to_increment] = vents[point_to_increment] + 1

        return len(
            [
                point
                for point in vents.keys()
                if vents[point] >= 2
            ]
        )

print("Sample input solution: ", solve("sample_input"))
print("Real input solution: ", solve("input"))
