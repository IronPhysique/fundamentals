milkshakes = {
    "Chocolate": 5,
    "Vanilla": 4,
    "Strawberry": 3.50,
    "Banana": 3,
    "Oreo": 6
}

while True:
    try:
        budget = int(input("Enter your budget: "))
        break
    except ValueError:
        print("Money only i dont take compliments (Enter a number).")

affordable = []
index = 1
print("You can afford these milkshakes:")
for shake, price in milkshakes.items():
    if price <= budget:
        affordable.append(shake)
        print(f"{index}. {shake} (£{price})")
        index += 1

if not affordable:
    print("You can't afford anything, get out.")
else:
    while True:
        try:
            choice_index = int(input("Enter the number of the milkshake you want: "))
            if 1 <= choice_index <= len(affordable):
                selected_shake = affordable[choice_index - 1]
                print(f"Here is the {selected_shake} milkshake now get out.")
                break
            else:
                print("Please select a valid number from the list.")
        except ValueError:
            print("Please enter a valid number.")
