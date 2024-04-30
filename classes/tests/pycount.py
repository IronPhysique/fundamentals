
def count(sequence, item):
    sum = 0
    for n in sequence:
        if n == item:
            sum += 1
    return sum

def test_count_integers():
    data = [1, 2, 2, 3, 4, 2, 2]
    assert count(data, 2) == 4

def test_count_strings():
    data = ["apple", "banana", "apple", "cherry"]
    assert count(data, "apple") == 2  
