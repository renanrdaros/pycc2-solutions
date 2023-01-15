# Exercise 7-8. Deli

sandwich_orders = ["chicken", "egg", "tuna", "ham", "bacon"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich} sandwich.")

print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
