from aoc_input import AOCInput
from pprint import pprint
puzzle_input = AOCInput()
test_input = AOCInput(filename='test_input.txt')

def ans(data):
    largest_seat_id = 0
    for boarding_pass in data:
        rows = list(range(128))
        cols = list(range(8))
        first_seven = boarding_pass[:7]
        for character in first_seven:
            if character == "F":
                rows = rows[:len(rows)//2]
            elif character == 'B':
                rows = rows[len(rows)//2:]
        last_three = boarding_pass[-3:]
        for character in last_three:
            if character == 'R':
                cols = cols[len(cols)//2:]
            elif character == 'L':
                cols = cols[:len(cols)//2]
        seat_id = (rows.pop() * 8) + cols.pop()
        if seat_id > largest_seat_id:
            largest_seat_id = seat_id
    return largest_seat_id


def test(data):
    return ans(data) == 820


def main():
    if test(test_input.get_input):
        answer1 = ans(puzzle_input.get_input)
        print(f'The answer for puzzle one is {answer1}')
    else:        print('Test failed')

if __name__ == "__main__":
    main()
