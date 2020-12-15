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


@log_wrap(entering, exiting)
def ans(starting_numbers: list):
    """ans() finds answer to the puzzle"""
    numbers_spoken = dict()
    for x  in range(1,2021):
        logger.debug(f'x = {x}')
        if x < len(starting_numbers) + 1:
            numbers_spoken[x] = starting_numbers[x-1]
            logger.debug(f'less than len starting numbers, added {starting_numbers[x-1]}')
        else:
            logger.debug('x greater than len start nums')
            ns_values = list(numbers_spoken.values())
            number = numbers_spoken[x-1]
            logger.debug(f'number = {number}')
            if number in ns_values[:x-2]:
                logger.debug(f'number exists: {number}')
                keys_of_matches = []
                for k, v in numbers_spoken.items():
                    if v == numbers_spoken[x-1]:
                        keys_of_matches.append(k)
                logger.debug(f'keys_of_matches = {keys_of_matches}')
                pop_key = keys_of_matches.pop()
                logger.debug(f'popped {pop_key} from list')
                max_key = max(keys_of_matches)
                logger.debug(f'max_key = {max_key}')
                age = (x-1)-max_key
                logger.debug(f'age = {age}')
                numbers_spoken[x] = age
                logger.debug(f'added {numbers_spoken[x]}')
            else:
                logger.debug(f'first_time: {number}')
                numbers_spoken[x] = 0
                logger.debug(f'added {numbers_spoken[x]}')
    return numbers_spoken[2020]


@log_wrap(entering, exiting)
def main():
    # puzzle = [0,3,6]
    puzzle = [0,14,1,3,7,9]
    print(f"The answer for puzzle is {ans(puzzle)}")


if __name__ == "__main__":
    main()
