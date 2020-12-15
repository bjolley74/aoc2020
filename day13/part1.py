from aoc_input import AOCInput


# get_data section
def get_data(fn: str) -> tuple:
    data_in = AOCInput(filename=fn)
    data = data_in.get_input
    # insert logic to change data as necessary
    return int(data[0]), tuple([int(x) for x in data[1].split(',') if x != 'x'])


def ans(data_in: tuple):
    """ans() finds answer to the puzzle"""
    timestamp = data_in[0]
    bus_ids = data_in[1]
    departure_times = [(timestamp - (timestamp % x)) + x for x in bus_ids]
    min_depart_time = min(departure_times)
    min_index = departure_times.index(min_depart_time)
    min_bus_id = bus_ids[min_index]
    return min_bus_id * (min_depart_time - timestamp)


def test_ans(data_in: tuple) -> bool:
    """test ans() on test_input.txt"""
    result = ans(data_in)
    # set return to check that ans == expected result
    return result == 295


def main():
    # load_test_input
    test_input = get_data('test_input.txt')
    if test_ans(test_input):
        # if test passed then will load and run ans() with the puzzle input
        puzzle_input = get_data('puzzle_input.txt')
        answer = ans(puzzle_input)
        print(f'The answer for puzzle is {answer}')
    else:
        # prints if test failed
        print('Test failed')


if __name__ == "__main__":
    main()
