# Exercise 7-10. Dream Vacation

responses = {}

while True:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name] = response

    ask_again = input("\nWould you like to ask again? ")
    if ask_again.lower() in ["no", "nope", "n"]:
        break

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to visit {response}.")
