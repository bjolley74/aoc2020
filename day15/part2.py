from datetime import datetime

def ans(starting_numbers: list, stop: int):
    """ans() finds answer to the puzzle"""
    numbers_spoken = dict()
    for x  in range(1, stop):
        if x%100 == 0:
            print(f'working on loop {x}, time now = {datetime.now()}')
        if x < len(starting_numbers) + 1:
            numbers_spoken[x] = starting_numbers[x-1]
        else:
            ns_values = list(numbers_spoken.values())
            number = numbers_spoken[x-1]
            if number in ns_values[:x-2]:
                keys_of_matches = []
                for k, v in numbers_spoken.items():
                    if v == numbers_spoken[x-1]:
                        keys_of_matches.append(k)
                pop_key = keys_of_matches.pop()
                max_key = max(keys_of_matches)
                age = (x-1)-max_key
                numbers_spoken[x] = age
            else:
                numbers_spoken[x] = 0
    return numbers_spoken[stop]


def main():
    start = datetime.now()
    print(f'starting time = {start}')
    # puzzle = [0,3,6]
    puzzle = [0,14,1,3,7,9]
    print(f"The answer for puzzle is {ans(puzzle, 30000000)}")
    end = datetime.now()
    print(f'end time = {end}')
    print(f'elapsed time = {end - start}')



if __name__ == "__main__":
    main()
