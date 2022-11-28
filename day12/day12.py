from pathlib import Path

test_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""


def part_1(puzzle_input: str) -> float:
    parsed = [line.split("-") for line in puzzle_input.splitlines()]
    destinations = {item: [] for pair in parsed for item in pair}
    for (start, end) in parsed:
        destinations[start].append(end)
        destinations[end].append(start)
    incomplete_paths = [["start"]]
    completed_paths = []
    while incomplete_paths:
        current_path = incomplete_paths.pop()
        for destination in destinations[current_path[-1]]:
            if destination == "end":
                completed_paths.append(current_path + ["end"])
            elif not destination.islower() or destination not in current_path:
                incomplete_paths.append(current_path + [destination])
    return len(completed_paths)


def part_2(puzzle_input: str) -> float:
    parsed = [line.split("-") for line in puzzle_input.splitlines()]
    destinations = {item: [] for pair in parsed for item in pair}
    for (start, end) in parsed:
        destinations[start].append(end)
        if start != "start":
            destinations[end].append(start)
    incomplete_paths = [["start"]]
    completed_paths = []
    while incomplete_paths:
        current_path = incomplete_paths.pop()
        for destination in destinations[current_path[-1]]:
            if destination == "end":
                completed_paths.append(current_path + ["end"])
            elif (
                    destination.islower()
                    and destination in current_path
                    and not current_path[0] == "doubled"
            ):
                incomplete_paths.append(["doubled"] + current_path + [destination])
            elif not destination.islower() or destination not in current_path:
                incomplete_paths.append(current_path + [destination])
    return len(completed_paths)


def test_part_1():
    assert part_1(test_input) == 10


def test_part_2():
    assert part_2(test_input) == 36


def main():
    print("🎄 Advent of code 2021 🎄")
    puzzle_input = Path("input.txt").read_text()
    test_part_1()
    print(f"Part 1: {part_1(puzzle_input)}")
    test_part_2()
    print(f"Part 2: {part_2(puzzle_input)} - 96801 is too high")


if __name__ == "__main__":
    main()
