from pathlib import Path

def get_input(filename):
    fn = Path('c:/users/bobby/mypython/aoc/aoc2020/day4/' + filename)
    with open(fn, 'r') as file:
        lines = file.read().replace(' ',',')
    lines = lines.replace('\n\n', '|')
    lines = lines.replace('\n',  ',')
    lst = lines.split('|')
    passports = []
    for line in lst:
        split_on_comma = line.split(',')
        temp_dict = dict()
        for item in split_on_comma:
            key, value = item.split(':')
            temp_dict[key] = value
        passports.append(temp_dict)
    return passports

def det_valid(passport:dict) -> bool:
    validity = True
    required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for field in required_fields:
        if field not in passport:
            validity = False 
    return validity

def test_func(key: str, value: str)-> bool:
    results = []
    if key == 'byr' or key == 'iyr' or key == 'eyr':
        if key == "byr":
            start = 1920
            end = 2002
        elif key == 'iyr':
            start = 2010
            end = 2020
        else:
            start = 2020
            end = 2030
        try:
            results.append(start <= int(value) <= end)
        except ValueError:
                #print(f'error - value = {value}')
                results.append(False)
    elif key == 'hgt':
        unit = value[-2:]
        try:
            measurement = int(value[:-2])
        except ValueError:
            results.append(False)
        if unit == 'cm':
            results.append(150 <= measurement <= 193)
        elif unit == 'in':
            results.append(59 <= measurement <= 76)
        else:
            results.append(False)
    elif key == 'hcl':
        valid_hcl_characters = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        results.append(value[0]=='#')
        results.append(len(value[1:]) == 6)
        for character in value[1:]:
            results.append(character in valid_hcl_characters)
    elif key == 'ecl':
        valid_ecl_codes = ['amb','blu','brn', 'gry', 'grn', 'hzl', 'oth']
        results.append(len(value) == 3 and value in valid_ecl_codes)
    elif key == 'pid':
        results.append(value.isnumeric() and len(value) == 9)
    return all(results)


def det_valid2(passport:dict)-> bool:
    test_results = dict()
    if not det_valid(passport):
        return False
    for k, v in passport.items():
        test_results[k] = test_func(k, v)
    return all(test_results.values())

def ans1(passports: list)-> int:
    count_valid = 0
    for passport in passports:
        if det_valid(passport):
            count_valid += 1
    return count_valid

def ans2(passports: list)-> int:
    count_valid = 0
    for passport in passports:
        if det_valid2(passport):
            count_valid += 1
    return count_valid

def test1():
    passports = get_input('test.input')
    answer = ans1(passports)
    return answer == 2

def test2():
    valid_passports = get_input('valid_passports.txt')
    invalid_passports = get_input('invalid_passports.txt')
    len_valid = len(valid_passports)
    answer_valid = ans2(valid_passports)
    answer_invalid = ans2(invalid_passports)
    return answer_valid == len_valid and answer_invalid == 0

def main():
    if test1():
        answer1 = ans1(get_input('puzzle_input.txt'))
        print(f'The answer for puzzle one is {answer1}')
    else:
        print('Test1 failed')
    if test2():
        answer2 = ans2(get_input('puzzle_input.txt'))
        print(f'The answer for puzzle two is {answer2}')
    else:
        print('Test2 failed')


if __name__ == "__main__":
    main()
    #test = get_input('puzzle_input.txt')
    #pprint(test)