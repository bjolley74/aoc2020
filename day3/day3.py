from aoc_input import AOCInput

def expand_pattern(input_file: tuple)-> tuple:
    '''
    returns tuple of the input expanded to the right
    '''
    #calculate expansion, number of rows * length of a row to make sure did not get IndexError
    expansion = len(input_file) * len(input_file[0])
    new_pattern = []
    for row in input_file:
        new_pattern.append(row*expansion)
    return tuple(new_pattern)

def ans1(my_input: tuple)-> int:
    '''
    function to find number of trees along a three over one down path
    trees are represented in the input as a '#'
    '''
    answer = 0
    #call expand pattern to extend pattern to the right
    new_input = expand_pattern(my_input)
    position = 0
    #iterate through each row
    for row in new_input:
        #check if first row then add three to the position
        if position == 0:
            position += 3
        else:
            #if not the first row will check if the row at the position is a 'tree'
            if row[position] == '#':
                #if a tree will add one to answer
                answer+= 1
            #increase postion by three to get the next position
            position += 3
    return answer

def ans2(my_input: tuple, right: int, down: int) -> int:
    '''
    function to find number of trees along different slopes path
    trees are represented in the input as a '#'
    '''
    answer = 0
    #call expand pattern to extend pattern to the right
    new_input = expand_pattern(my_input)
    position = 0
    #iterate through every 'down' number of rows
    for row in range(0,len(new_input),down):
        #check if first row then add right to the position
        if row == 0:
            position += right
        else:
            #if not the first row will check if the row at the position is a 'tree'
            if new_input[row][position] == '#':
                #if a tree will add one to answer
                answer+= 1
            #increase postion by right to get the next position
            position += right
    return answer

def test1()->bool:
    '''
    tests the program for the first puzzle against the test input given on the page
    to make sure I get same answer as that is given on adventofcode.com
    '''
    test = AOCInput(filename='test_input.txt')
    test_input = tuple(test.get_input)
    ans = ans1(test_input)
    return ans == 7

def test2(slopes: tuple) -> bool:
    '''
    tests the program for the first puzzle against the test input given on the page
    to make sure I get same answer as that is given on adventofcode.com
    '''
    test = AOCInput(filename='test_input.txt')
    test_input = tuple(test.get_input)
    lst = []
    ans = 1
    for slope in slopes:
        appending = ans2(test_input,slope[0],slope[1])
        lst.append(appending)
    for num in lst:
        ans *= num
    return ans == 336

def main():
    puzzle_input = AOCInput()
    if test1() is True:
        print(f'Answer for puzzle one is {ans1(puzzle_input.get_input)}')
    else:
        print('Test1 failed')
    slopes = ((1,1),(3,1),(5,1),(7,1),(1,2))
    if test2(slopes) is True:
        lst_of_nums = []
        for slope in slopes:
            lst_of_nums.append(ans2(puzzle_input.get_input,slope[0],slope[1]))
        ans_2 = 1
        for num in lst_of_nums:
            ans_2 *= num
        print(f'Answer for puzzled two is {ans_2}')
    else:
        print(f'Test2 failed.')


if __name__ == "__main__":
    main()