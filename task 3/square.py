
number = 1

while number <= 100:
    square = number * number
    print(f"{number} squared is {square}")
    
    if square > 2000:
        break
    
    number += 1

