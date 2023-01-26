# Exercise 4-13. Buffet

foods = ("pizza", "falafel", "carrot cake", "cannoli", "ice cream")

print("Original menu:")
for food in foods:
    print(f"  - {food}")

# cannot assign a new value to a tuple's element
# foods[1] = "cheeseburger"
# foods[3] = "hot dog"

# but we can assign a new value to the variable that represents the tuple
foods = ("pizza", "cheeseburger", "carrot cake", "hot dog", "ice cream")

print("\nRevised menu:")
for food in foods:
    print(f"  - {food}")

