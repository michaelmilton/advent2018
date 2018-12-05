from typing import List, Set

def get_nums(file: str) -> List:
    with open(file, 'r') as f:
        nums = [int(line.strip()) for line in f]
    return nums

def get_frequency(freq_updates: List, start_num: int = 0) -> int:
    freq = start_num
    frequencies = {0}
    for num in freq_updates:
        freq += num
        if freq in frequencies:
            print('Recurrent frequency: ' + str(freq))
        frequencies.add(freq)
    return freq

assert get_frequency([1,1,1]) == 3
assert get_frequency([1,1,-2]) == 0
assert get_frequency([-1,-2,-3]) == -6
assert get_frequency([1,-2,3,1])

if __name__ ==  '__main__':
    file = 'data/day01_input.txt'
    nums = get_nums(file)
    freq = get_frequency(nums)
    print("Frequency: " + str(freq))

    print(get_frequency([1,1,-2,1,1]))
