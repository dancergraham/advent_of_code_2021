from pathlib import Path

test_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


# test_input = """<{([{{}}[<[[[<>{}]]]>[]]"""


def part_1(puzzle_input: str) -> float:
    lines = [line for line in puzzle_input.splitlines()]
    answer = 0
    stack = []
    for line in lines:
        for paren in line:
            if paren in "[{(<":
                stack.append(paren)
            elif stack[-1] == {">": "<",
                               ")": "(",
                               "]": "[",
                               "}": "{",
                               }[paren]:
                stack.pop()
            else:
                score = {">": 25137,
                         ")": 3,
                         "]": 57,
                         "}": 1197,
                         }
                answer += score[paren]
                break
    return answer


def part_2(puzzle_input: str) -> float:
    answers = []
    score = {"<": 4,
             "(": 1,
             "[": 2,
             "{": 3,
             }
    close_to_open = {">": "<",
                     ")": "(",
                     "]": "[",
                     "}": "{",
                     }
    for line in puzzle_input.splitlines():
        stack = []
        for paren in line:
            if paren in "[{(<":
                stack.append(paren)
            elif stack[-1] == close_to_open[paren]:
                stack.pop()
            else:
                break
        else:
            # line is incomplete
            print(line)
            print(stack)
            completion_score = 0
            while stack:
                completion_score *= 5
                completion_score += score[stack.pop()]
            answers.append(completion_score)
            print(completion_score)
    answers.sort()
    answer = answers[len(answers) // 2]
    return answer


def test_part_1():
    assert part_1(test_input) == 26397


def test_part_2():
    assert part_2(test_input) == 288957


def main():
    print("🎄 Advent of code 2021 🎄")
    puzzle_input = Path("input.txt").read_text()
    print(f"Part 1: {part_1(puzzle_input)}")
    print(f"Part 2: {part_2(puzzle_input)}")


if __name__ == "__main__":
    main()
