from pathlib import Path

test_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


def part_1(puzzle_input: str) -> float:
    numbers = [x for x in puzzle_input.splitlines()]
    counter = [0 for bit in numbers[0]]
    for number in numbers:
        for i, digit in enumerate(number):
            counter[i] += int(digit)
    values = len(numbers)
    gamma = int("".join(str(int((digit / values) > 0.5)) for digit in counter), 2)
    epsilon = int("".join(str(int((digit / values) < 0.5)) for digit in counter), 2)
    return gamma * epsilon


def part_2(puzzle_input: str) -> float:
    parsed = (int(x) for x in puzzle_input.splitlines())
    answer = 0
    for current in parsed:
        ...
    return answer


def test_part_1():
    assert part_1(test_input) == 198


def test_part_2():
    assert part_2(test_input) == 0


def main():
    puzzle_input = Path("input.txt").read_text()
    print(part_1(puzzle_input))
    print(part_2(puzzle_input))


if __name__ == "__main__":
    main()
