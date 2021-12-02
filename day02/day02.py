from collections import Counter
from pathlib import Path

test_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def part_1(puzzle_input: str) -> float:
    parsed = [line for line in puzzle_input.splitlines()]
    counter = Counter()
    for line in parsed:
        direction, distance = line.split()
        counter[direction] += int(distance)
    return counter["forward"] * (counter["down"] - counter["up"])


def part_2(puzzle_input: str) -> float:
    parsed = [line for line in puzzle_input.splitlines()]
    horizontal = 0
    depth = 0
    aim = 0
    for line in parsed:
        direction, distance = line.split()
        distance = int(distance)
        if direction == "forward":
            horizontal += distance
            depth += aim * distance
        elif direction == "up":
            aim -= distance
        elif direction == "down":
            aim += distance
    return abs(horizontal * depth)


def test_part_1():
    assert part_1(test_input) == 150


def test_part_2():
    assert part_2(test_input) == 900


def main():
    puzzle_input = Path("input.txt").read_text()
    print(part_1(puzzle_input))
    print(part_2(puzzle_input))


if __name__ == "__main__":
    main()
