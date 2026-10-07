def add(a, b):
    # Bug: Returns wrong value
    return a + b 

def test_add():
    assert add(2, 3) == 5