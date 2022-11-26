from collections import Counter
from pathlib import Path

test_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def parser(puzzle_input: str):
    for line in puzzle_input.splitlines():
        start, stop = line.split(" -> ")
        x0, y0 = start.split(",")
        x1, y1 = stop.split(",")
        yield ((int(x0), int(y0)), (int(x1), int(y1)))


def part_1(puzzle_input: str, part=1) -> float:
    parsed = parser(puzzle_input)
    point_counter = Counter()
    for (x0, y0), (x1, y1) in parsed:
        if (x0 == x1) or (y0 == y1) or part == 2:
            delta_x = x1 - x0
            delta_y = y1 - y0
            dx = 0 if not delta_x else int(delta_x / abs(delta_x))
            dy = 0 if not delta_y else int(delta_y / abs(delta_y))
            for i in range(max(abs(delta_x), abs(delta_y))):
                point_counter.update([(x0 + i * dx, y0 + i * dy)])
            point_counter.update([(x1, y1)])
    return len([v for v in point_counter.values() if v > 1])


def test_part_1():
    assert part_1(test_input) == 5
    assert part_1(test_input, part=2) == 12


def main():
    print("🎄 Advent of code 2021 🎄")
    puzzle_input = Path("input.txt").read_text()
    print(f"Part 1: {part_1(puzzle_input)}")
    print(f"Part 2: {part_1(puzzle_input, part=2)}")


if __name__ == "__main__":
    main()
