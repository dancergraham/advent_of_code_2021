from collections import Counter
from itertools import pairwise
from pathlib import Path

test_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


def part_1(puzzle_input: str) -> float:
    parsed = [x for x in puzzle_input.splitlines()]
    template = parsed[0]
    mapping = dict()
    for line in parsed[2:]:
        (first, second), insertion = line.split(" -> ")
        mapping[(first, second)] = insertion
    for step in range(10):
        new_template = []
        for a, b in pairwise(template):
            new_template.append(a)
            new_template.append(mapping[(a, b)])
        new_template.append(b)
        template = new_template.copy()
    count = Counter(template)
    mini, *_, maxi = sorted(count.values())
    return maxi - mini


def part_2(puzzle_input: str) -> float:
    parsed = [x for x in puzzle_input.splitlines()]
    template = pairwise(parsed[0])
    final_value = parsed[0][-1]
    mapping = dict()
    for line in parsed[2:]:
        (first, second), insertion = line.split(" -> ")
        mapping[(first, second)] = [(first, insertion), (insertion, second)]
    count = Counter({k: 0 for k in mapping})
    for pair in template:
        count[pair] += 1
    for step in range(40):
        new_count = Counter({x: 0 for x in count})
        for pair, number in count.items():
            new_count[mapping[pair][0]] += number
            new_count[mapping[pair][1]] += number
        count = new_count.copy()
    answer_count = Counter({x[0]: 0 for x in count})
    for pair, number in count.items():
        answer_count[pair[0]] += number
    answer_count[final_value] += 1
    mini, *_, maxi = sorted(answer_count.values())
    return maxi - mini


def test_part_1():
    assert part_1(test_input) == 1588


def test_part_2():
    assert part_2(test_input) == 2188189693529


def main():
    print("🎄 Advent of code 2021 🎄")
    puzzle_input = Path("input.txt").read_text()
    print(f"Part 1: {part_1(puzzle_input)}")
    print(f"Part 2: {part_2(puzzle_input)}")


if __name__ == "__main__":
    main()
