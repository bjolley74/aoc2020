from aoc_input import AOCInput


def ans_1(list_in: list) -> int:
    num_valid = 0
    for min_letter, max_letter, letter, pw in str_generator(list_in):
        print(min_letter, max_letter, letter, pw)

def str_generator(list_in: list) -> tuple:
    list1 = []
    for line in list_in:
        list1.append(line.split())
    for line in list1:
        min_letter, max_letter = line[0].split('-')
        letter = line[1][0:1]
        password = line[2]
        yield (min_letter , max_letter, letter, password)

def test_ans1() -> bool:
    test_input = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
    return ans_1(test_input) == 2

if __name__ == "__main__":
    if test_ans1():
        puzzle_input = AOCInput('puzzle_input.txt')
        print(f'answer for puzzle one is {ans_1(puzzle_input)}\n')
    else:
        print(f'test of ans_1() failed.')