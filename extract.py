from unittest import TestCase, main


def add(a, b):
    return a + b


class Test(TestCase):
    def test_add(self):
        self.assertEqual(add(5, 6), 11)


if __name__ == "__main__":
    main()
