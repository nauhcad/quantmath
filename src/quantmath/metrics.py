import numpy as np
import pandas as pd
from typing import Sequence
from math import isfinite


def ensure_nonempty(data:Sequence[float], variable_name=None):
    if variable_name == None:
        variable_name = 'data'
    if len(data) == 0:
        raise ValueError(f'{variable_name} sequence must be non-empty!')
    return True

def ensure_finite(data:Sequence[float], variable_name=None):
    if all(not isfinite(x) for x in data):
        raise ValueError(f'All entries in {variable_name} sequence must be finite!')     
    return True 

def ensure_equal_length(a:Sequence[float], b:Sequence[float], a_name = None, b_name= None):
    if a_name != None and b_name != None:
        error_msg = f"{a_name} and {b_name} aren't the same length!"
    else:
        error_msg = 'data arrays not the same length'
    if len(a) != len(b):
        raise ValueError(error_msg)
    return True

def arithmetic_mean(data:Sequence[float]) -> float:
    '''
    Returns the arithmetic average. 
    Validation: non-empty, all finite
    
    Input: data:Sequence[Float]
    Returns: float representing the arithmetic mean of the data
    '''
    
    if ensure_nonempty(data, 'data') and ensure_finite(data, 'data'):
        return sum(data)/len(data)
    
    
def weighted_mean(data:Sequence[float], weights:Sequence[float]) -> float:
    '''
    Returns the weighted mean of data. 
    Validation: non-empty, all finite, and weights must be same legnth as data.
    
    Input: data:Sequence[Float], weights:Sequence[float]
    Returns: float representing the arithmetic mean of the data
    '''
    
    for seq_label, label in zip(['data', 'weights'], [data, weights]):
        _ = ensure_nonempty(label, seq_label) and ensure_finite(label, seq_label)
        
    ensure_equal_length(data, weights, 'data', 'weights')
        
    return sum([a*b for a, b in zip(data, weights)])/len(data)


    
        
    

