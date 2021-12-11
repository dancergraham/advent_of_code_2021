from pathlib import Path

test_input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
fgae cfgab fg bagce""".replace("|\n", "|")


def part_1(puzzle_input: str) -> float:
    outputs = [line.split(" |")[1] for line in puzzle_input.splitlines()]
    answer = 0
    for output in outputs:
        print(output)
        answer += len([item for item in output.split() if len(item) in [2, 3, 4, 7]])
    return answer


def part_2(puzzle_input: str) -> float:
    parsed = (line.split(" |") for line in puzzle_input.splitlines())
    answer = 0
    digits = {}
    for pattern, output in parsed:
        digits[1], digits[7], digits[4], *_others, digits[8] = sorted(
            map(set, pattern.split()), key=len)
        _235 = _others[:3]
        _069 = _others[3:]
        for digit in _069:
            if len(digit.difference(digits[4])) == 2:
                digits[9] = digit
            elif len(digit.union(digits[1])) == 7:
                digits[6] = digit
            else:
                digits[0] = digit
        for digit in _235:
            if len(digit.difference(digits[4])) == 3:
                digits[2] = digit
            elif len(digit.difference(digits[7])) == 2:
                digits[3] = digit
            else:
                digits[5] = digit
        result = []
        for out in output.split():
            out = set(out)
            for value, pattern in digits.items():
                if out == pattern:
                    result.append(str(value))
        answer += int("".join(result))
    return answer


def test_part_1():
    assert part_1(test_input) == 26


def test_part_2():
    assert part_2(test_input) == 61229


def main():
    print("🎄 Advent of code 2021 🎄")
    puzzle_input = Path("input.txt").read_text()
    print(f"Part 1: {part_1(puzzle_input)}")
    print(f"Part 2: {part_2(puzzle_input)}")


if __name__ == "__main__":
    main()
