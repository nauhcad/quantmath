from src.quantmath import metrics
from math import isclose

def test_arithmetic_mean():
    data = [1,2,3,4,5]
    
    actual = metrics.arithmetic_mean(data)
    
    assert isclose(actual, 3, rel_tol=1e-9)
    
def test_weighted_mean():
    data =    [1,2,3,4]
    weights = [3,4,5,1]
    
    actual = metrics.weighted_mean(data, weights)
    
    assert isclose(actual, 7.5, rel_tol=1e-9)

def main():
    test_arithmetic_mean()
    test_weighted_mean()