from aoc_input import AOCInput
import logging

#    logger set up
log_file = "part2.log"
log_level = logging.DEBUG
f = '%(asctime)-15s: %(levelname)-8s: %(message)s'
logging.basicConfig(level=log_level, filename=log_file, filemode='w+', format=f)
logger = logging.getLogger(__name__)

def log_wrap(pre, post):
    """Wrapper"""
    def decorate(func):
        """Decorater"""
        def call(*args,**kwargs):
            """Actual Wrapper"""
            pre(func)
            result = func(*args, **kwargs)
            post(func)
            return result
        return call
    return decorate


def entering(func):
    """Pre function logging"""
    logger.debug(f"entered {func.__name__}")

def exiting(func):
    """Post function logging"""
    logger.debug(f"exiting {func.__name__}")

@log_wrap(entering, exiting)
def lists(lst: list)-> list:
    pass

# get_data section
@log_wrap(entering, exiting)
def get_data(fn: str) -> list:
    data_in  = AOCInput(filename=fn)
    data = data_in.get_input
    logger.debug(f'data = {data}')
    #insert logic to change data as necessary
    output = [int(x) for x in data]
    return output


@log_wrap(entering, exiting)
def ans(data_in: list, invalid_number: int) -> int:
    """ans() finds answer to the puzzle"""
    for step in range(2,len(data_in)):
        for x in range(len(data_in)-step):
            test_range = data_in[x: x+step]
            if sum(test_range) == invalid_number:
                min_num = min(test_range)
                max_num = max(data_in[x: x+step])
    return min_num + max_num

@log_wrap(entering, exiting)
def test_ans(data_in: list, test_part1) -> bool:
    """test ans() on test_input.txt"""
    result = ans(data_in, test_part1)
    # set return to check that ans == expected result
    return result == 62

@log_wrap(entering, exiting)
def main():
    #load_test_input
    test_input = get_data('test_input.txt')
    if test_ans(test_input, 127):
        #if test passed then will load and run ans() with the puzzle input
        puzzle_input = get_data('puzzle_input.txt')
        answer = ans(puzzle_input, 70639851)
        print(f'The answer for puzzle is {answer}')
    else:
        #prints if test failed
        print('Test failed')

if __name__ == "__main__":
    main()
