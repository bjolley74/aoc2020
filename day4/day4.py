def get_input(filename):
    with open(filename, 'r') as file:
        lines = file.read().replace(' ',', ')
    passports = lines.split('\n\n')
    passports_out = []
    for p in passports:
        a = p.split(', ')
        my_dict = {}
        for b in a:
            if '\n' in b:
                c = b.split('\n')
                for d in c:
                    e, f = d.split(':')
                    my_dict[e] = f
            else:
                c, d = b.split(':')
                my_dict[c] = d
        passports_out.append(my_dict)
    return passports_out

def det_valid(passport:dict) -> bool:
    validity = True
    required_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for field in required_fields:
        if field not in passport:
            validity = False 
    return validity

def ans(passports: list)-> int:
    count_valid = 0
    for passport in passports:
        if det_valid(passport):
            count_valid += 1
    return count_valid


def test1():
    passports = get_input('test.input')
    answer = ans1(passports)
    return answer == 2

def test2():
    return False

def main():
    if test1():
        answer1 = ans(get_input('puzzle_input.txt'))
        print(f'The answer for puzzle one is {answer1}')
    else:
        print('Test1 failed')
    if test2():
        answer2 = ans(get_input('puzzle_input.txt'))
        print(f'The answer for puzzle two is {answer2}')
    else:        print('Test2 failed')

if __name__ == "__main__":
    main()
