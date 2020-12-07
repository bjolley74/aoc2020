def my_input(filename='puzzle_input.txt'):
    with open(filename, 'r') as file:
        data = file.read()
    data = data.replace('\n',',')
    data = data.replace(',,', '|')
    data = data.split('|')
    return [x.split(',') for x in data]


test_input = my_input('test_input.txt')
puzzle_input = my_input('puzzle_input.txt')

# ans() finds answer to the puzzle
def ans(data_in: list):
    sum = 0
    for group in data_in:
        group_answers = set()
        for individual in group:
            for question in individual:
                group_answers.add(question)
        group_total = len(group_answers)
        sum += group_total
    return sum

#tests ans on test input
def test_ans(data_in: list) -> bool:
    return ans(data_in) == 11

def main():
    if test_ans(test_input):
        print(f'The answer for the puzzle is {ans(puzzle_input)}')
    else:
        print('Test failed')
    

if __name__ == "__main__":
    main()
