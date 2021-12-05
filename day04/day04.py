from pathlib import Path

test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


def part_1(puzzle_input: str) -> float:
    def complete(line):
        """checks that all elements of line are in `drawn` from the outer scope"""
        return all(x in drawn for x in line)

    parsed = (x for x in puzzle_input.splitlines())
    numbers = [x for x in next(parsed).split(",")]
    boards = []
    for current in parsed:
        if not current:
            boards.append([])
            continue
        boards[-1].append(current.strip().split())
    for board in boards:
        columns = [[row[i] for row in board] for i, _ in enumerate(board)]
        board.extend(columns)
    drawn = set()
    answers = []

    while boards:
        finished = []
        number = numbers.pop(0)
        drawn.add(number)
        for i, board in enumerate(boards):
            if any(complete(line) for line in board):
                winning_numbers = {item for row in board for item in row}
                winning_numbers.difference_update(drawn)
                answer = sum(map(int, winning_numbers)) * int(number)
                answers.append(answer)
                finished.append(i)
        [boards.pop(i) for i in finished[::-1]]
    return answers[0], answers[-1]


def part_2(puzzle_input: str) -> float:
    parsed = [x for x in puzzle_input.splitlines()]
    answer = 0
    for current in parsed:
        ...
    return answer


def test_part_1():
    _part_1, _part_2 = part_1(test_input)
    assert _part_1 == 4512
    assert _part_2 == 1924


def main():
    print("🎄 Advent of code 2021 🎄")
    print("🎄 Day 04 🎄")
    puzzle_input = Path("input.txt").read_text()
    _part_1, _part_2 = part_1(puzzle_input)
    print(f"Part 1: {_part_1}")
    print(f"Part 2: {_part_2}")


if __name__ == "__main__":
    main()
