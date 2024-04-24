budget = int(input("How much you got?"))
shakes = {
    "chocolate" : 4,
    "vanilla": 3,
    "oreo": 5,
    "banana": 2.50,
    "strawberry": 3.50
}

affordable = [shake for shake, price in shakes.items() if price <= budget]

if not affordable:
    print("Get out now")
else:
    print("Here is what you can afford: " + ", ".join(affordable))