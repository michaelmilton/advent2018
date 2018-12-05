from typing import List

def get_nums(file: str) -> List:
    with open(file, 'r') as f:
        nums = [int(line.strip()) for line in f]
    return nums