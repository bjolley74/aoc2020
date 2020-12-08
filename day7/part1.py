'''
question: How many bag colors can eventually contain at least one shiny gold bag?
'''

from aoc_input import AOCInput
from pprint import pprint

def get_data(test=False):
    if test:
        input_file = AOCInput(filename='test_input.txt')
        data = input_file.get_input
    else:
        input_file = AOCInput()
        data = input_file.get_input
    data_out = dict()
    for line in data:
        a, b = line.split('contain')
        a = a.replace('bags',"")
        b = b.strip(' ')
        if b == 'no other bags.':
            data_out[a] = 0
        else:
            c = b.split(',')
            d = dict()
            for item in c:
                item = item.strip('.')
                item = item.strip('bags')
                num = int(item[0:2])
                item = item[2:]
                d[item.strip(' ')] = num
            data_out[a.strip(' ')] = d
    return data_out

test_input = get_data(test=True)
puzzle_input = get_data()

# ans() finds answer to the puzzle
def ans(data_in: list, target='shiny gold'):
    bags_that_can_hold_target = []
    for key, value in data_in.items():
        if value != 0:
            if target in value.keys():
                bags_that_can_hold_target.append(key)
    for bag in bags_that_can_hold_target:
        if bag != []:
            bags = ans(data_in, target=bag)
            for b in bags:
                bags_that_can_hold_target.append(b)
    return bags_that_can_hold_target

#tests ans on test input
def test_ans(data_in: list) -> bool:
    answer = len(set(ans(data_in)))
    return answer == 4

def main():
    if test_ans(test_input):
        print('working on puzzle_input...')
        answer = ans(puzzle_input)
        print(f'The answer for puzzle is {len(set(answer))}')
    else:
        print('Test failed')

if __name__ == "__main__":
    main()
