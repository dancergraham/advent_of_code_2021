from pathlib import Path

test_input = """16,1,2,0,4,2,7,1,2,14"""


def part_1(puzzle_input: str) -> float:
    crabs = [int(x) for x in puzzle_input.split(",")]

    def distance_sum(position):
        return sum(abs(crab - position) for crab in crabs)

    position = min(range(min(crabs),
                         max(crabs) + 1
                         ),
                   key=distance_sum
                   )
    return distance_sum(position)


def part_2(puzzle_input: str) -> float:
    crabs = [int(x) for x in puzzle_input.split(",")]

    def distance_sum(position):
        return sum(sum(range(abs(crab - position) + 1))
                   for crab in crabs)

    position = min(range(min(crabs),
                         max(crabs) + 1
                         ),
                   key=distance_sum
                   )
    return distance_sum(position)


def test_part_1():
    assert part_1(test_input) == 37


def test_part_2():
    assert part_2(test_input) == 168


def main():
    print("🎄 Advent of code 2021 🎄")
    puzzle_input = Path("input.txt").read_text()
    print(f"Part 1: {part_1(puzzle_input)}")
    print(f"Part 2: {part_2(puzzle_input)}")


if __name__ == "__main__":
    main()
