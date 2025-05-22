from src.math_operation import addition, subtraction 

def test_add():
    assert addition(2,3) == 5
    assert addition(-4, 10) == 6
    
def test_minus():
    assert subtraction(5, 10)== -5
    assert subtraction(-6, 3)== -9