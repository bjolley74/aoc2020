import os
from glob import glob
from shutil import copyfile

def write_file(file_obj):
    file_obj.write('from aoc_input import AOCInput\n\n')
    file_obj.write('test_input = AOCInput("test_input.py")\n')
    file_obj.write('puzzle_input = AOCInput()\n\n')
    file_obj.write('# ans() finds answer to the puzzle\n')
    file_obj.write('def ans(data_in: list):\n    return 0\n\n')
    file_obj.write('#tests ans on test input\n')
    file_obj.write('def test_ans(data_in: list) -> bool:\n    return False\n\n')
    file_obj.write('def main():\n')
    file_obj.write('    if test_ans(test_input):\n')
    file_obj.write('        answer = ans(puzzle_input)\n')
    file_obj.write("        print(f'The answer for puzzle is {answer}')\n")
    file_obj.write("    else:\n")
    file_obj.write("        print('Test failed')\n\n")
    file_obj.write('if __name__ == "__main__":\n')
    file_obj.write('    main()\n')
    return "file written"

def main():
    max_num = 0
    directories = glob('day*')
    for folder in directories:
        num = int(folder[3:])
        if num > max_num:
            max_num = num
    new_folder_name = 'day' + str(max_num + 1) + '/'
    #make new directory for the new day
    try:
        os.mkdir(new_folder_name)
    except (IOError, OSError) as err:
        print(f'\nError occured writing {new_folder_name}\n')
        raise err
    #change path into newly created directory
    try:
        os.chdir(new_folder_name)
    except (IOError, OSError) as err:
        print(f'\nError occured changing directory to {new_folder_name}\n')
    #write new .py file for part 1
    try:
        with open('part1.file','w') as python_file:
            write_file(python_file)
    except (IOError, OSError) as err:
        print(f'\nError occured while writing part1.py\n')
        raise err
    #write new .py file for part 2
    try:
        with open('part2.file','w') as python_file:
            write_file(python_file)
    except (IOError, OSError) as err:
        print(f'\nError occured while writing part2.py\n')
        raise err
    #write new puzzle_input.txt
    try:
        with open('puzzle_input.txt', 'w') as input_file:
            input_file.write('')
    except (IOError, OSError) as err:
        print('\nError occured opening puzzle_input.txt.\n')
        raise err
    #copy aoc_input.py from parent directory
    try:
        copyfile('../aoc_input.py', 'aoc_input.py')
    except (IOError, OSError) as err:
        print('\nError occured copying aoc_input.py. Check parent directory for file!\n')
        raise err

if __name__ == '__main__':
    main()