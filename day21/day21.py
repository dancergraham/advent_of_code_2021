from functools import lru_cache
from pathlib import Path

test_input = """Player 1 starting position: 4
Player 2 starting position: 8
"""


def deterministic_d100():
    roll = 1
    while True:
        yield roll
        roll += 1
        if roll == 101:
            roll = 1


def part_1(puzzle_input: str) -> float:
    positions = [int(x[-1]) for x in puzzle_input.splitlines()]
    points = [0, 0]
    die = deterministic_d100()
    rolls = 0
    while max(points) < 1000:
        throws = [next(die), next(die), next(die)]
        i = rolls % 2
        throwsum = sum(throws)
        positions[i] = (positions[i] + throwsum) % 10 or 10
        points[i] += positions[i]
        rolls += 3
        ...
    return min(points) * rolls


def part_2(puzzle_input: str) -> float:
    @lru_cache
    def number_of_wins(positions, wins, points, player):
        if points[0] >= 21:
            return [1, 0]
        elif points[1] >= 21:
            return [0, 1]
        else:
            for roll in [1, 2, 3]:
                new_positions = list(positions)
                new_positions[player] += roll
                new_positions[player] = new_positions[player] or 10
                new_points = list(points)
                new_points[player] += new_positions[player]
                win1, win2 = number_of_wins(tuple(new_positions),
                                            wins,
                                            tuple(new_points),
                                            (player + 1) % 2
                                            )
                wins = (wins[0] + win1, wins[1] + win2)
            return wins

    positions = tuple([int(x[-1]) for x in puzzle_input.splitlines()])
    wins = (0, 0)
    points = (0, 0)
    wins = number_of_wins(positions, wins, points, 0)

    return max(wins)


def test_part_1():
    assert part_1(test_input) == 739785


def test_part_2():
    assert part_2(test_input) == 444356092776315


def main():
    print("🎄 Advent of code 2021 🎄")
    puzzle_input = Path("input.txt").read_text()
    test_part_1()
    print(f"Part 1: {part_1(puzzle_input)}")
    test_part_2()
    print(f"Part 2: {part_2(puzzle_input)}")


if __name__ == "__main__":
    main()
