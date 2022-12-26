# Exercise 4-11. My Pizzas, Your Pizzas

my_pizzas = ["pepperoni", "ham", "pineapple", "bacon"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("mushrooms")
friend_pizzas.append("broccoli")

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(f"  - {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"  - {pizza}")
