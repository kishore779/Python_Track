import pytest

def add(a, b):
    return a + b

def test_add():
    assert add(2,3) == 5

@pytest.mark.parametrize(
        "a, b, result",
        [
            (2,4,6),
            (0,9,9),
            (10,10,20),
            (10,-3,7)
        ]
)
def test_multiple_cases(a, b, result):
    assert add(a, b) == result

if __name__ == "__main__":
    import pytest
    pytest.main()