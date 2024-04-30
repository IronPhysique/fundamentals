def count(sequence, item):
    count = 0
    for element in sequence:
        if element == item:
            count += 1
        return count
        