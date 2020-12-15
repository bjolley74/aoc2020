import logging

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
    data_in  = AOCInput(filename=fn)
    data = data_in.get_input
    # insert logic to change data as necessary
    output = data
    return output


@log_wrap(entering, exiting)
def ans(starting_numbers: list):
    """ans() finds answer to the puzzle"""
    numbers_spoken = dict()
    for x  in range(2020):
        logger.debug(f'x = {x}')
        if x < len(starting_numbers):
            numbers_spoken[x] = starting_numbers[x]
            logger.debug(f'less than len starting numbers, added {starting_numbers[x]}')
        else:
            logger.debug('x greater than len start nums')
            ns_values = list(numbers_spoken.values())
            if numbers_spoken[x-1] in ns_values[:-2]:
                logger.debug(f'number exists: {numbers_spoken[x-1]}')
                keys_of_matches = []
                for k, v in numbers_spoken.items():
                    if v == numbers_spoken[x-1]:
                        keys_of_matches.append(k)
                logger.debug(f'keys_of_matches = {keys_of_matches}')
                logger.debug(f'popped {keys_of_matches.pop()} from list')
                max_key = max(keys_of_matches)
                age = x-max_key
                numbers_spoken[x] = age
            else:
                logger.debug(f'first_time: {numbers_spoken[x-1]}')
                numbers_spoken[x] = 0
    return numbers_spoken[2019]


@log_wrap(entering, exiting)
def main():
    test = [0,3,6]
    puzzle = [0,14,1,3,7,9]
    print(f"The answer for puzzle is {ans(test)}")


if __name__ == "__main__":
    main()
