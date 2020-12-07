import string
from collections import Counter

def my_input(filename='puzzle_input.txt'):
    with open(filename, 'r') as file:
        data = file.read()
    data = data.replace('\n',',')
    data = data.replace(',,', '|')
    data = data.split('|')
    data = [x.split(',') for x in data]
    output = []
    for group in (data):
        g = []
        for individual in group:
            i=[]
            for char in individual:
                i.append(char)
            g.append(i)
        output.append(g)
    return output

test_input = my_input('test_input.txt')
puzzle_input = my_input('puzzle_input.txt')

# ans() finds answer to the puzzle
def ans(data_in: list) -> int:
    sum = 0
    for group in data_in:
        num_in_group = len(group)
        if num_in_group == 1:
            sum += len(group[0])
        else:
            answers = []
            for individual in group:
                for char in individual:
                    answers.append(char)
            numbers = Counter(answers)
            for value in numbers.values():
                if value == num_in_group:
                    sum += 1
    return sum

#tests ans on test input
def test_ans(data_in: list) -> bool:
    return ans(data_in) == 6

def main():
    if test_ans(test_input):
        print(f'The answer for the puzzle is {ans(puzzle_input)}')
    else:
        print('Test failed')

if __name__ == "__main__":
    main()
