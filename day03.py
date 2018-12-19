import numpy as np
from typing import List, Tuple, NamedTuple
import re

example_input = '#4 @ 976,493: 24x21'

class Claim(NamedTuple):
    idx : int
    from_left : int
    from_top : int
    width : int
    height : int

def parse_claim(input: str):
    tightened_input = re.sub(' *#*','', input)
    split_input = re.split('[@,:x]', tightened_input)
    input_ints = [int(x) for x in split_input]
    return Claim(*input_ints)

    output = np.copy(input)
    input_r_size, input_c_size = input.shape
    final_r_size, final_c_size = size

    # Add zeroes to rows
    if final_r_size <= input_r_size:
        pass
    else:
        output = np.insert(output, 
                    input_r_size, 
                    np.zeros((final_r_size - input_r_size, input_c_size)), 
                    axis= 0
        )

    # Add zeroes to columns
    if final_c_size <= input_c_size:
        pass
    else:
        output = np.insert(output, 
                    input_c_size, 
                    np.zeros((final_c_size-input_c_size, final_r_size)), 
                    axis= 1
        )
    
    return output

def resize_claim(input: np.array, size: Tuple, side: str = 'left') -> np.array:
    output = np.copy(input)
    input_r_size, input_c_size = input.shape
    final_r_size, final_c_size = size
    
    row_idx = 0
    col_idx = 0

    if side == 'right':
        row_idx = input_r_size
        col_idx = input_c_size

    # Add zeroes to rows
    if final_r_size <= input_r_size:
        pass
    else:
        output = np.insert(output, 
                    row_idx, 
                    np.zeros((final_r_size - input_r_size, input_c_size)), 
                    axis= 0
        )

    # Add zeroes to columns
    if final_c_size <= input_c_size:
        pass
    else:
        output = np.insert(output, 
                    col_idx, 
                    np.zeros((final_c_size-input_c_size, final_r_size)), 
                    axis= 1
        )
    
    return output

def get_max_dimension(input: List[np.array]) -> Tuple:
    max_x = 0
    max_y = 0
    
    for array in input:
        array_x, array_y = array.shape
        if array_x > max_x:
            max_x = array_x
        if array_y > max_y:
            max_y = array_y
    
    return (max_x, max_y)

def create_array_from_claim(claim: Claim) -> np.array:
    pass

def sum_claims(input: List[np.array]) -> np.array:
    pass

def count_zeroes(input: np.array) -> int:
    pass

def read_inputs(file) -> List[Claim]:
    with open(file, 'r') as f:
        inputs = f.readlines()
    return [parse_claim(claim) for claim in inputs]

if __name__ == '__main__':
    filename = 'data/day03_input.txt'
    inputs = read_inputs(filename)