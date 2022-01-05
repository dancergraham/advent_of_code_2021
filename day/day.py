from pathlib import Path

test_input = """"""


def part_1(puzzle_input: str) -> float:
    parsed = [x for x in puzzle_input.splitlines()]
    answer = 0
    for current in parsed:
        ...
    return answer


def part_2(puzzle_input: str) -> float:
    parsed = [x for x in puzzle_input.splitlines()]
    answer = 0
    for current in parsed:
        ...
    return answer


def test_part_1():
    assert part_1(test_input) == 0


def test_part_2():
    assert part_2(test_input) == 0


def main():
    print("🎄 Advent of code 2021 🎄")
    puzzle_input = Path("input.txt").read_text()
    test_part_1()
    print(f"Part 1: {part_1(puzzle_input)}")
    test_part_2()
    print(f"Part 2: {part_2(puzzle_input)}")


if __name__ == "__main__":
    main()
