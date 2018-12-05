from typing import List, Set
from itertools import cycle, chain

def get_nums(file: str) -> List:
    with open(file, 'r') as f:
        nums = [int(line.strip()) for line in f]
    return nums

def get_final_frequency(freq_updates: List, start_num: int = 0) -> int:
    return sum(chain([start_num], freq_updates))

assert get_final_frequency([1,1,1]) == 3
assert get_final_frequency([1,1,-2]) == 0
assert get_final_frequency([-1,-2,-3]) == -6
assert get_final_frequency([1,-2,3,1])

def get_duplicate_frequency(freq_updates: List, start_num: int = 0) -> int: 
    freq = start_num
    frequencies = {0}
    for num in cycle(freq_updates):
        freq += num
        if freq in frequencies:
            break
        frequencies.add(freq)
    return freq

assert get_duplicate_frequency([1, -1]) == 0
assert get_duplicate_frequency([3, 3, 4, -2, -4]) == 10
assert get_duplicate_frequency([-6, 3, 8, 5, -6]) == 5
assert get_duplicate_frequency([7, 7, -2, -7, -4]) == 14

if __name__ ==  '__main__':
    file = 'data/day01_input.txt'
    nums = get_nums(file)
    
    freq = get_final_frequency(nums)
    print("Final frequency: " + str(freq))

    first_dup = get_duplicate_frequency(nums)
    print("First duplicate frequency: " + str(first_dup))
