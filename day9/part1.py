from aoc_input import AOCInput
import logging
from copy import deepcopy

#    logger set up
log_file = "file.log"
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
def my_zip(lst):
    lst2 = deepcopy(lst)
    zipped_list = [(x, y) for x in lst for y in lst2 if x != y]
    logger.debug(f'zipped_list: {zipped_list}')
    return zipped_list

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
def ans(data_in: list, preamble_length: int) -> int:
    """ans() finds answer to the puzzle"""
    preamble = data_in[:preamble_length]
    data_list = data_in[preamble_length:]
    next_num = data_list.pop(0)
    logger.debug(f'preamble = {preamble}')
    logger.debug(f'next_num = {next_num}')
    while next_num:
        data_zip = my_zip(preamble)
        logger.debug(f'data_zip = {data_zip}')
        pairs_list = [x for x in data_zip if x[0] + x[1] == next_num]
        logger.debug(f'pairs_list = {pairs_list}')
        if len(pairs_list) == 0:
            return next_num
        else:
            preamble.pop(0)
            preamble.append(next_num)
            next_num = data_list.pop(0)
    return next_num

@log_wrap(entering, exiting)
def test_ans(data_in: list) -> bool:
    """test ans() on test_input.txt"""
    result = ans(data_in, 5)
    # set return to check that ans == expected result
    return result == 127

@log_wrap(entering, exiting)
def main():
    #load_test_input
    test_input = get_data('test_input.txt')
    if test_ans(test_input):
        #if test passed then will load and run ans() with the puzzle input
        puzzle_input = get_data('puzzle_input.txt')
        answer = ans(puzzle_input, 25)
        print(f'The answer for puzzle is {answer}')
    else:
        #prints if test failed
        logger.debug('Test failed')

if __name__ == "__main__":
    main()
