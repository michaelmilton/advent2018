import numpy as np
from typing import List, Tuple

def parse_input(input: str) -> np.array:
    pass

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
    pass

def sum_claims(input: List[np.array]) -> np.array:
    pass

def count_zeroes(input: np.array) -> int:
    pass