from advent_util import get_nums
from typing import List

def get_letter_counts(s: str) -> List[int]:
    letters = set(s)
    counts = [len([x for x in s if x == letter])
                for letter in letters
                ]
    return counts

def has_double(s:str) -> bool:
    counts = get_letter_counts(s)
    return 2 in counts

assert has_double('aabbb') == True
assert has_double('bbb') == False
assert has_double('abcdef') == False

def double_count(input_list: List[str]) -> int:
    return sum([1 for s in input_list if has_double(s) == True])

assert double_count(['aabb','ab','abaa']) == 1

def has_triple(s:str) -> bool:
    counts = get_letter_counts(s)
    return 3 in counts

assert has_triple('ababab') == True

def triple_count(input_list: List[str]) -> int:
    return sum([1 for s in input_list if has_triple(s) == True])

assert double_count(['aabb','ab','abaa']) == 1

def get_rudimentary_checksum(input_list: List[str]) -> int:
    return double_count(input_list) * triple_count(input_list)

test_list = ["abcdef","bababc","abbcde","abcccd","aabcdd","abcdee","ababab"]
assert get_rudimentary_checksum(test_list) == 12

if __name__ == '__main__':
    with open('data/day02_input.txt', 'r') as f:
        ss = [line.strip() for line in f] 

    print(get_rudimentary_checksum(ss))
    