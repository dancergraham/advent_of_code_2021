from pathlib import Path

test_input = """3,4,3,1,2"""


def part_1(puzzle_input: str) -> float:
    fishes = [int(x) for x in puzzle_input.split(",")]
    for day in range(256):
        newfish = [8 for fish in fishes if fish == 0]
        fishes = [6 if fish == 0 else fish - 1 for fish in fishes]
        fishes.extend(newfish)
    return len(fishes)


def part_2(puzzle_input: str) -> float:
    parsed = [x for x in puzzle_input.splitlines()]
    answer = 0
    for current in parsed:
        ...
    return answer


def test_part_1():
    assert part_1(test_input) == 5934


def test_part_2():
    assert part_2(test_input) == 0


def main():
    print("🎄 Advent of code 2021 🎄")
    puzzle_input = Path("input.txt").read_text()
    print(f"Part 1: {part_1(puzzle_input)}")
    print(f"Part 2: {part_2(puzzle_input)}")


if __name__ == "__main__":
    main()
