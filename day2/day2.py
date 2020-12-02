from aoc_input import AOCInput


def ans_1(list_in: list) -> int:
    num_valid = 0
    for min_letter, max_letter, letter, pw in str_generator(list_in):
        count = pw.count(letter)
        if min_letter <= count <= max_letter:
            num_valid += 1
    return num_valid

def str_generator(list_in: list) -> tuple:
    list1 = []
    for line in list_in:
        list1.append(line.split())
    for line in list1:
        min_letter, max_letter = line[0].split('-')
        letter = line[1][0:1]
        password = line[2]
        yield (int(min_letter) , int(max_letter), letter, password)

def ans_2(list_in: list) -> int:
    num_valid = 0
    for first_letter, second_letter, letter, pw in str_generator(list_in):
        pos_1 = pw[first_letter - 1]
        pos_2 = pw[second_letter - 1]
        if  (pos_1 == letter or  pos_2 == letter) and pos_1 != pos_2:
            num_valid += 1
    return num_valid

def test_ans1() -> bool:
    test_input = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
    return ans_1(test_input) == 2

def test_ans2() -> bool:
    test_input = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc']
    return ans_2(test_input) == 1

if __name__ == "__main__":
    if test_ans1():
        puzzle_input = AOCInput(filename='puzzle_input.txt')
        print(f'\nAnswer for puzzle one is {ans_1(puzzle_input.get_input)}\n')
    else:
        print(f'test of ans_1() failed.')
    if test_ans2():
        print(f'Answer for puzzle two is {ans_2(puzzle_input.get_input)}\n')
    else:
        print("test of ans_2() failed.")