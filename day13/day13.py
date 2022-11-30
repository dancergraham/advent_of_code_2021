from pathlib import Path

test_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


def part_1(puzzle_input: str) -> float:
    points = []
    folds = []
    for line in puzzle_input.splitlines():
        try:
            points.append(eval(line))
        except SyntaxError:
            if line:
                folds.append(line.split(" ")[-1].split("="))
    folded = set()
    fold = folds[0]
    for point in points:
        x, y = point
        if fold[0] == "y" and y > int(fold[1]):
            y = 2 * int(fold[1]) - y
        elif fold[0] == "x" and x > int(fold[1]):
            x = 2 * int(fold[1]) - x
        folded.add((x, y))

    return len(folded)


def part_2(puzzle_input: str) -> float:
    points = []
    folds = []
    for line in puzzle_input.splitlines():
        try:
            points.append(eval(line))
        except SyntaxError:
            if line:
                folds.append(line.split(" ")[-1].split("="))
    folded = set()
    for fold in folds:
        for point in points:
            x, y = point
            if fold[0] == "y" and y > int(fold[1]):
                y = 2 * int(fold[1]) - y
            elif fold[0] == "x" and x > int(fold[1]):
                x = 2 * int(fold[1]) - x
            folded.add((x, y))
        points, folded = folded, set()
    for y in range(6):
        for x in range(40):
            if (x, y) in points:
                print("X", end="")
            else:
                print(" ", end="")
        print()
    return 0


def test_part_1():
    assert part_1(test_input) == 17


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
