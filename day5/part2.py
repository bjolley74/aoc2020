from aoc_input import AOCInput
from pprint import pprint
puzzle_input = AOCInput()
test_input = AOCInput(filename='test_input.txt')

def my_zip(list1, list2):
    output = []
    for item1 in list1:
        for item2 in list2:
            output.append((item1, item2))
    return tuple(output)

def ans(data):
    seat_ids = []
    rows_cols = my_zip(list(range(128)),list(range(8)))
    all_possible_seat_ids = [x * 8 + y for x, y in rows_cols]
    missing_ids = []
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
        seat_ids.append((rows.pop() * 8) + cols.pop())
    for seat_id in all_possible_seat_ids:
        if seat_id not in seat_ids:
            missing_ids.append(seat_id)
    for seat_id in missing_ids:
        plus_one = seat_id + 1
        minus_one = seat_id - 1
        if plus_one in seat_ids and minus_one in seat_ids:
            print(seat_id)
            ans = seat_id
    return ans


def main():
    answer2 = ans(puzzle_input.get_input)
    print(f'The answer for puzzle one is {answer2}')

if __name__ == "__main__":
    main()
