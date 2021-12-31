from copy import deepcopy
from pathlib import Path

test_input = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""


def part_1(puzzle_input: str) -> float:
    board = [list(line) for line in puzzle_input.splitlines()]
    width = len(board[0])
    height = len(board)
    answer = 0
    for step in range(10000):
        # print(f"\nstep {step}")
        # print("\n".join("".join(l) for l in board))
        new_board = deepcopy(board)
        for row in range(height):
            for col in range(width):
                if (board[row][col] == ">") and (board[row][(col + 1) % width] == "."):
                    new_board[row][col] = "."
                    new_board[row][(col + 1) % width] = ">"
        board1 = deepcopy(new_board)
        for row in range(height):
            for col in range(width):
                if (board1[row][col] == "v") and (board1[(row + 1) % height][col] == "."):
                    new_board[row][col] = "."
                    new_board[(row + 1) % height][col] = "v"
        if board == new_board:
            break
        board = new_board

    return step + 1


def part_2(puzzle_input: str) -> float:
    parsed = [x for x in puzzle_input.splitlines()]
    answer = 0
    for current in parsed:
        ...
    return answer


def test_part_1():
    assert part_1(test_input) == 58


def test_part_2():
    assert part_2(test_input) == 0


def main():
    print("🎄 Advent of code 2021 🎄")
    puzzle_input = Path("input.txt").read_text()
    print(f"Part 1: {part_1(puzzle_input)}")
    print(f"Part 2: {part_2(puzzle_input)}")


if __name__ == "__main__":
    main()
