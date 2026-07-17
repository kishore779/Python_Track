import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(8,2),10)

if __name__ == "__main__":
    unittest.main()
