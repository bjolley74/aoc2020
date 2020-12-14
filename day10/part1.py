from aoc_input import AOCInput
import logging
from copy import deepcopy

#    logger set up
log_file = "day10.log"
log_level = logging.DEBUG
f = '%(asctime)-15s| %(levelname)-8s| %(message)s'
logging.basicConfig(level=log_level, filename=log_file, filemode='w+', format=f)
logger = logging.getLogger(__name__)


def log_wrap(pre, post):
    """Wrapper"""
    def decorate(func):
        """Decorater"""
        def call(*args, **kwargs):
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


# get_data section
@log_wrap(entering, exiting)
def get_data(fn: str) -> list:
    data_in = AOCInput(filename=fn)
    data = data_in.get_input
    # insert logic to change data as necessary
    return [int(x) for x in data]


@log_wrap(entering, exiting)
def det_next_adapter(adapters: list, joltage: int) -> int:
    """determines the next adapter"""
    if len(adapters) < 1:
        return None
    elif len(adapters) == 1:
        return adapters[0]
    else:
        possible_adapters = [x for x in adapters if x > joltage and (x - 1) - joltage <= 3]
        logger.debug(f'possible adapters: {possible_adapters}')
        return min(possible_adapters)


@log_wrap(entering, exiting)
def ans(data_in: list):
    """ans() finds answer to the puzzle"""
    joltage = 0
    adapters = deepcopy(data_in)
    one_jolt_difference = []
    three_jolt_difference = []
    adapter = det_next_adapter(adapters, joltage)
    adapters.remove(adapter)
    count = 0
    for _ in range(len(data_in)):
        logger.debug(f'joltage: {joltage}, adapter: {adapter}')
        if adapter - joltage == 1:
            one_jolt_difference.append(adapter)
            logger.debug(f'one jolt diff: {adapter - joltage}')
        elif adapter - joltage == 3:
            three_jolt_difference.append(adapter)
            logger.debug(f'three jolt diff: {adapter - joltage}')
        else:
            logger.warning(f'other diff found: {adapter - joltage}')
        joltage = adapter
        adapter = det_next_adapter(adapters, adapter)
        adapters.remove(adapter)
        count += 1
    device = max(data_in) + 3
    l3joltd.append(device)
    l1joltd = len(one_jolt_difference)
    l3joltd = len(three_jolt_difference)
    product = l1joltd * l3joltd
    logger.debug(f'len 1 jolt diff: {l1joltd}, len 3 jolt diff: {l3joltd}, product: {product}')
    return product


@log_wrap(entering, exiting)
def test_ans(data_in: list) -> bool:
    """test ans() on test_input.txt"""
    result = ans(data_in)
    # set return to check that ans == expected result
    return result == 220


@log_wrap(entering, exiting)
def main():
    # load_test_input
    small_test = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    small_test_ans = ans(small_test)
    print(f'small_test_ans = {small_test_ans}')
    if small_test_ans == 35:
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
