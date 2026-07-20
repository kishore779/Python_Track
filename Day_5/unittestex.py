import unittest

def div(a : int, b : int) -> float:
    try:
        return a / b
    except ZeroDivisionError as e:
        return ZeroDivisionError

class TestAdd(unittest.TestCase):
    """
    Checks normal division
    """
    def test_numbers(self):
        self.assertEqual(div(8,2),4)

    """
    Checks for negative outputs
    """
    def test_negative(self):
        self.assertEqual(div(5,-1),-5)

    """
    Checks result for zero
    """
    def test_zero_case(self):
        self.assertEqual(div(0,5), 0)
    
    """
    Checks for ZeroDivion Error
    """
    def test_zero_div_error(self):
        self.assertEqual(div(5,0), ZeroDivisionError)


if __name__ == "__main__":
    unittest.main()
