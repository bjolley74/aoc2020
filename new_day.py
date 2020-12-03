import os
from glob import glob
from shutil import copyfile

def main():
    max_num = 0
    directories = glob('day*')
    for folder in directories:
        num = int(folder[3:])
        if num > max_num:
            max_num = num
    new_folder_name = 'day' + str(max_num + 1) + '/'
    new_file_name = 'day' + str(max_num + 1) + '.py'
    try:
        os.mkdir(new_folder_name)
    except (IOError, OSError) as err:
        print(f'\nError occured writing {new_folder_name}\n')
        raise err
    try:
        os.chdir(new_folder_name)
    except (IOError, OSError) as err:
        print(f'\nError occured changing directory to {new_folder_name}\n')
    try:
        with open(new_file_name,'w') as python_file:
            python_file.write('from aoc_input import AOCInput\n\n')
            python_file.write('def ans1():\n    return 0\n\n')
            python_file.write('def ans2():\n    return 0\n\n')
            python_file.write('def test1():\n    return False\n\n')
            python_file.write('def test2():\n    return False\n\n')
            python_file.write('def main():\n')
            python_file.write('    if test1():\n')
            python_file.write('        answer1 = ans1()\n')
            python_file.write("        print(f'The answer for puzzle one is {answer1}')\n")
            python_file.write("    else:")
            python_file.write("        print('Test1 failed')\n")
            python_file.write('    if test2():\n')
            python_file.write('        answer2 = ans2()\n')
            python_file.write("        print(f'The answer for puzzle two is {answer2}')\n")
            python_file.write("    else:")
            python_file.write("        print('Test2 failed')\n\n")
            python_file.write('if __name__ == "__main__":\n')
            python_file.write('    main()\n')
    except (IOError, OSError) as err:
        print(f'\nError occured while writing {new_file_name}\n')
        raise err
    try:
        input_file = open('puzzle_input.txt', 'w')
    except (IOError, OSError) as err:
        print('\nError occured opening puzzle_input.txt.\n')
        raise err
    finally:
        input_file.close()
    try:
        copyfile('../aoc_input.py', 'aoc_input.py')
    except (IOError, OSError) as err:
        print('\nError occured copying aoc_input.py. Check parent directory for file!\n')
        raise err

if __name__ == '__main__':
    main()