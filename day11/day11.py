import contextlib
from pathlib import Path

test_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


def enumerate2d(np_array):
    """Pure python 2D equivalent of numpy.ndenumerate"""
    for y, row in enumerate(np_array):
        for x, element in enumerate(row):
            yield (x, y), element


class Octopus:
    def __init__(self, energy_level):
        self.energy_level = int(energy_level)
        self.flashes = 0
        self.has_flashed_this_step = False
        self.neighbours = []

    def __add__(self, other):
        self.energy_level += other
        if self.energy_level > 9 and not self.has_flashed_this_step:
            self.flash()

    def flash(self):
        self.flashes += 1
        self.has_flashed_this_step = True
        for neighbour in self.neighbours:
            neighbour += 1

    def end_step(self):
        if self.has_flashed_this_step:
            self.energy_level = 0
        self.has_flashed_this_step = False


def set_neighbours(grid):
    for (x, y), octopus in enumerate2d(grid):
        for x_position in [x - 1, x, x + 1]:
            if x_position == -1:
                continue
            for y_position in [y - 1, y, y + 1]:
                is_centre = x_position == x and y_position == y
                if y_position == -1 or is_centre:
                    continue
                with contextlib.suppress(IndexError):
                    octopus.neighbours.append(grid[y_position][x_position])


def part_1(puzzle_input: str) -> float:
    grid = [[Octopus(energy_level=x) for x in line] for line in puzzle_input.splitlines()]
    set_neighbours(grid)
    for _ in range(100):
        # print(f"\nAfter step {step + 1}:")
        for line in grid:
            for octopus in line:
                octopus += 1
        [octopus.end_step() for line in grid for octopus in line]
        # for line in grid:
        # print("".join(str(octopus.energy_level) for octopus in line))
    return sum(octopus.flashes for line in grid for octopus in line)


def part_2(puzzle_input: str) -> float:
    parsed = [x for x in puzzle_input.splitlines()]
    answer = 0
    for current in parsed:
        ...
    return answer


def test_part_1():
    assert part_1(test_input) == 1656


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
