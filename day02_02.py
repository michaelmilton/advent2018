from typing import Tuple, List, Set

def drop_diff_chars(strings: Tuple[str, str]) -> str:
    s1, s2 = strings
    char_length = len(s1)
    same_chars = ([s1[char_num] for char_num 
                    in range(char_length)
                    if s1[char_num] == s2[char_num]
                    ])
    return ''.join(same_chars)

assert drop_diff_chars(('abcd','abde')) == 'ab'

def get_common_letters(codes: List[str]) -> Set:
    code_length = get_code_length(codes)
    return {drop_diff_chars((s1, s2)) for s1 in codes for s2 in codes
            if len(drop_diff_chars((s1, s2))) == code_length -1
            }

def get_code_length(codes: List[str]) -> int:
    return len(codes[0])

if __name__ == '__main__': 
    with open('data/day02_input.txt', 'r') as f:
        codes = [line.strip() for line in f] 
    
    print(get_common_letters(codes))

