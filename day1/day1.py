#day 1 aoc puzzle
import copy
test_input = [1721, 979, 366, 299, 675, 1456]

def get_input() -> list:
    output = []
    with open('puzzle_input.txt', 'r') as f:
        line = f.readline().strip()
        while line:
            output.append(int(line))
            line = f.readline().strip()
    return output

def make_points(list_in: list):
    list_b = copy.deepcopy(list_in)
    for item1 in list_in:
        for item2 in list_b:
            if item1 != item2:
                yield item1, item2


def calc_ans(puzzle_list: list) -> int:
    for one, two in make_points(puzzle_list):
        if one + two == 2020:
            return one * two

if __name__ == "__main__":
    if calc_ans(test_input) == 514579:
        print("Please wait while I calculate answer...")
        puzzle_input = get_input()
        print(f'answer = {calc_ans(puzzle_input)}')
