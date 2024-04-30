import unittest

def count(sequence, item):
    sum = 0
    for n in sequence:
        if n == item:
            sum += 1
    return sum

class TestCountFunction(unittest.TestCase):
    def test_count_integers(self):
        data = [1, 2, 2, 3, 4, 2, 2]
        self.assertEqual(count(data, 2), 4)

    def test_count_strings(self):
        data = ["apple", "banana", "apple", "cherry"]
        self.assertEqual(count(data, "apple"), 2)

if __name__ == '__main__':
    unittest.main()
