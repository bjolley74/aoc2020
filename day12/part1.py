from aoc_input import AOCInput
import logging

#    logger set up
log_file = "day12.log"
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
    output = [(x[0:1],int(x[1:])) for x in data ]
    return output


@log_wrap(entering, exiting)
def ans(instructions: list):
    """ans() finds answer to the puzzle"""
    def log_pos(loop, pos):
        logger.debug(f'loop #: {loop}: pos: {pos}')
    def move(inst: list, direction:int, current_pos: list) -> list:
        logging.debug(f'inst: {inst}, direction: {direction}, current_pos {current_pos}')
        if (inst[0] == 'F' and direction == 90) or inst[0] =="E":
            logging.debug(f'move forward while facing east or east {inst[1]}')
            current_pos[0] += inst[1]
        elif (inst[0] == 'F' and direction == 270) or inst[0] == 'W':
            logging.debug(f'move forward while facing west or move west {inst[1]}')
            current_pos[0] -= inst[1]
        elif (inst[0] == 'F' and direction == 0) or inst[0] == 'N':
            logging.debug(f'move forward while facing north or move north {inst[1]}')
            current_pos[1] += inst[1]
        elif (inst[0] == "F" and direction == 180) or inst[0] == 'S':
            logging.debug(f'move forward while facing south or move south {inst[1]}')
            current_pos[1] -= inst[1]
        elif inst[0] == 'R':
            logging.debug(f'turn right {inst[1]}')
            direction += inst[1]
        elif inst[0] == 'L':
            logging.debug(f'turn right {inst[1]}')
            direction -= inst[1]
        else:
            logging.critical(f'wrong instruction received {inst}')
        if direction >= 360:
            direction -= 360
        elif direction < 0:
            direction += 360
        return (direction, current_pos)
    card_direction = 90
    position = [0, 0]
    log_pos(-1, position)
    count = 0
    for instruction in instructions:
        logging.debug(f'instruction: {instruction}')
        card_direction, position = move(instruction, card_direction, position)
        log_pos(count, position)
    return abs(position[0]) + abs(position[1])


@log_wrap(entering, exiting)
def main():
    # if test passed then will load and run ans() with the puzzle input
    print(f'The answer for puzzle is {get_data('puzzle_input.txt')}')


if __name__ == "__main__":
    main()
