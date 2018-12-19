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


def parse_input(input: str):
    tightened_input = re.sub(' *#*','', input)
    split_input = re.split('[@,:x]', tightened_input)
    input_ints = [int(x) for x in split_input]
    return Claim(*input_ints)

def resize_claim(input: np.matrix, size: Tuple) -> np.array:
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

def sum_claims(input: List[np.array]) -> np.array:
    pass

def count_zeroes(input: np.array) -> int:
    pass