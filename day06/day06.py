from collections import Counter
from pathlib import Path

test_input = """3,4,3,1,2"""


def part_1(puzzle_input: str, days=80) -> float:
    fishes = [int(x) for x in puzzle_input.split(",")]
    fish_counter = Counter({i: 0 for i in range(9)})
    fish_counter.update(fishes)
    for day in range(days):
        for i in range(9):
            fish_counter[i - 1] = fish_counter[i]
        fish_counter[8] = fish_counter[-1]
        fish_counter[6] += fish_counter[-1]
        fish_counter[-1] = 0
    return sum(fish_counter.values())


def part_2(puzzle_input: str) -> float:
    return part_1(puzzle_input, days=256)


def test_part_1():
    assert part_1(test_input) == 5934


def test_part_2():
    assert part_2(test_input) == 26984457539


def main():
    print("🎄 Advent of code 2021 🎄")
    puzzle_input = Path("input.txt").read_text()
    print(f"Part 1: {part_1(puzzle_input)}")
    print(f"Part 2: {part_2(puzzle_input)}")


if __name__ == "__main__":
    main()
