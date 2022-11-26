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


def oxygen_rating(numbers: list[str]):
    i = 0
    while len(numbers) > 1:
        ones = sum(int(num[i]) for num in numbers if num[i] == "1")
        most_common = "1" if (ones >= len(numbers) / 2) else "0"
        numbers = [n for n in numbers if n[i] == most_common]
        i += 1
    return numbers[0]


def co2_rating(numbers: list[str]):
    i = 0
    while len(numbers) > 1:
        ones = sum(int(num[i]) for num in numbers if num[i] == "1")
        most_common = "1" if (ones < len(numbers) / 2) else "0"
        numbers = [n for n in numbers if n[i] == most_common]
        i += 1
    return numbers[0]


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
    numbers = [x for x in puzzle_input.splitlines()]
    return int(oxygen_rating(numbers), 2) * int(co2_rating(numbers), 2)


def test_part_1():
    assert part_1(test_input) == 198


def test_part_2():
    assert part_2(test_input) == 230


def main():
    puzzle_input = Path("input.txt").read_text()
    print(part_1(puzzle_input))
    print(part_2(puzzle_input))


if __name__ == "__main__":
    main()
