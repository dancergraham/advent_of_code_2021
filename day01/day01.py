from pathlib import Path

test_input = """199
200
208
210
200
207
240
269
260
263"""


def part_1(puzzle_input: str) -> float:
    parsed = (int(x) for x in puzzle_input.splitlines())
    answer = 0
    previous = float("inf")
    for current in parsed:
        if current > previous:
            answer += 1
        previous = current
    return answer


def part_2(puzzle_input: str) -> float:
    parsed = [int(x) for x in puzzle_input.splitlines()]
    answer = 0
    for removed, added in zip(parsed[:-3:], parsed[3::], strict=True):
        if added > removed:
            answer += 1
    return answer


def test_part_1():
    assert part_1(test_input) == 7


def test_part_2():
    assert part_2(test_input) == 7


def main():
    puzzle_input = Path("input.txt").read_text()
    print(part_1(puzzle_input))
    print(part_2(puzzle_input))


if __name__ == "__main__":
    main()
