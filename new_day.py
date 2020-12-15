import os
from glob import glob
from shutil import copyfile
from pathlib import Path
try:
    target_dir = Path('c:/users/bobby/mypython/AOC/aoc2020')
except FileNotFoundError:
    target_dir = Path('~/mypython/aoc2020/')
current_directory = Path(os.getcwd())
if current_directory != target_dir:
    os.chdir(target_dir)

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
        copyfile('../template.py', 'part1.py')
    except (IOError, OSError) as err:
        print(f'\nError occured while writing part1.py\n')
        raise err
    #write new .py file for part 2
    try:
        copyfile('../template.py', 'part2.py')
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
    #write new test_input.txt
    try:
        with open('test_input.txt', 'w') as input_file:
            input_file.write('')
    except (IOError, OSError) as err:
        print('\nError occured opening test_input.txt.\n')
        raise err
    #copy aoc_input.py from parent directory
    try:
        copyfile('../aoc_input.py', 'aoc_input.py')
    except (IOError, OSError) as err:
        print('\nError occured copying aoc_input.py. Check parent directory for file!\n')
        raise err

if __name__ == '__main__':
    main()